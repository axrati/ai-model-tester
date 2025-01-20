from transformers import AutoModel, AutoTokenizer
from transformers.tokenization_utils_base import BatchEncoding
import torch
from lib.corpus import corpus
import random
from typing import Union, Literal
from dataclasses import dataclass
from lib.model_config import ModelConfig
import time
from datetime import datetime, timedelta
import pytz
from lib.globals import date_string, uid


@dataclass
class GeneratedString:
    tokenized_data: BatchEncoding
    string: str
    size: int


@dataclass
class RunStat:
    id: str
    index: int
    cycle_id: str
    stage: Literal["tokenizing", "inference"]
    start: str
    end: str
    tokens: int
    seconds: int
    model_name: str
    permutations: int
    runs: int
    device: Literal["cuda", "cpu"]


class Model:
    def __init__(
        self,
        model_name: ModelConfig,
        device: Union["cuda", "cpu", "auto"] = "auto",
        local_model_force=False,
    ):
        """
        Initializes Model.

        Args:
            model_name (ModelConfig): The config of the Model.
            device (str): The device to run the model on. Options are:
                - "cuda": Run on GPU if available.
                - "cpu": Run on CPU.
                - "auto": Automatically select GPU if available, otherwise CPU.
            local_model_force (bool): Whether to force loading the model from a local directory only.
                If True, the method will not attempt to download the model from Hugging Face Hub.
        """
        print(f"Loading {model_name.name}...", end="\r")
        # Load the tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name.name, trust_remote_code=True, local_files_only=local_model_force
        )
        self.model = AutoModel.from_pretrained(
            model_name.name, trust_remote_code=True, local_files_only=local_model_force
        )
        self.model.eval()
        print(f"Loading {model_name.name} complete.", end="\r")
        # Set user device setting
        if device == "auto":
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        else:
            self.device = device
        self.model.to(self.device)

    def generate_string_of_token_length(self, amount: int) -> GeneratedString:
        """
        Generate strings to match a given token length
        """
        text_corpus = corpus()
        # Start with amount to text... This *should* be < tokens given that letters != tokens
        base = "".join([random.choice(text_corpus) for i in range(amount)])
        size = len(
            self.tokenizer(base, padding=True, truncation=True, return_tensors="pt").to(
                self.device
            )["input_ids"][0]
        )
        while size < amount:
            ADDITIVE = 250
            for ad in range(ADDITIVE):
                base = base + random.choice(text_corpus)
            size = len(
                self.tokenizer(
                    base, padding=True, truncation=True, return_tensors="pt"
                ).to(self.device)["input_ids"][0]
            )
            print(
                f"""AMT : {amount}    SIZE: {size}""",
                end="\r",
            )

        tokenized = self.tokenizer(
            base, padding=True, truncation=True, return_tensors="pt"
        ).to(self.device)

        return GeneratedString(tokenized_data=tokenized, string=base, size=size)

    def embed(self, texts: list[str]) -> bool:
        """
        Embeds a list of texts using model on GPU if available.

        Args:
            texts (list of str): List of strings to embed.

        Returns:
            torch.Tensor: Tensor of embeddings with shape (len(texts), embedding_dim).
        """
        try:
            with torch.no_grad():
                for txt in texts:
                    inputs = self.tokenizer(
                        [txt], padding=True, truncation=True, return_tensors="pt"
                    ).to(self.device)
                    outputs = self.model(**inputs)
                    embeddings = outputs.last_hidden_state.mean(dim=1)
            return True
        except Exception as e:
            print(f"Model embedding failed. \n{str(e)}")
            return False

    def embed_timed(
        self, texts: list[str], model_config: ModelConfig, tokens: int
    ) -> list[RunStat]:
        """
        Embeds a list of texts using model on GPU if available.

        Args:
            texts (list of str): List of strings to embed.

        Returns:
            torch.Tensor: Tensor of embeddings with shape (len(texts), embedding_dim).
        """
        try:
            runstats = []
            with torch.no_grad():
                outputs = {}
                idxx = 0
                for txt_idx in range(len(texts)):
                    # ~~ Tokenizer implementation ~~
                    cycle_id = uid()
                    reference_datetime = datetime.now()
                    reference_perf = time.perf_counter()
                    start_time_perf = time.perf_counter()
                    inputs = self.tokenizer(
                        [texts[txt_idx]],
                        padding=True,
                        truncation=True,
                        return_tensors="pt",
                    ).to(self.device)
                    end_time_perf = time.perf_counter()
                    end_datetime = reference_datetime + timedelta(
                        seconds=(end_time_perf - reference_perf)
                    )

                    reference_start_string = date_string(reference_datetime)
                    reference_end_string = date_string(end_datetime)

                    seconds = end_time_perf - start_time_perf
                    runstats.append(
                        RunStat(
                            id=uid(),
                            stage="tokenizing",
                            start=reference_start_string,
                            end=reference_end_string,
                            tokens=tokens,
                            seconds=seconds,
                            index=idxx,
                            model_name=model_config.name,
                            cycle_id=cycle_id,
                            permutations=model_config.permutations,
                            runs=model_config.runs,
                            device=self.device.type,
                        )
                    )
                    idxx += 1

                    # ~~ Inference implementation ~~
                    reference_datetime = datetime.now()
                    reference_perf = time.perf_counter()
                    start_time_perf = time.perf_counter()
                    outputs = self.model(**inputs)
                    end_time_perf = time.perf_counter()
                    end_datetime = reference_datetime + timedelta(
                        seconds=(end_time_perf - reference_perf)
                    )
                    reference_start_string = date_string(reference_datetime)
                    reference_end_string = date_string(end_datetime)
                    seconds = end_time_perf - start_time_perf
                    runstats.append(
                        RunStat(
                            id=uid(),
                            stage="inference",
                            start=reference_start_string,
                            end=reference_end_string,
                            tokens=tokens,
                            seconds=seconds,
                            index=idxx,
                            model_name=model_config.name,
                            cycle_id=cycle_id,
                            permutations=model_config.permutations,
                            runs=model_config.runs,
                            device=self.device.type,
                        )
                    )

                embeddings = outputs.last_hidden_state.mean(dim=1)
            return runstats
        except Exception as e:
            print(f"Model embedding failed. \n{str(e)}")
            return False
