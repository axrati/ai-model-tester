from lib.model import Model
from lib.model_config import ModelConfig
from typing import List
import math
import random
from lib.timer import batch_timer
from datetime import datetime
from lib.globals import date_string
from lib.model import RunStat
import json
from dataclasses import asdict


class ModelRunner:
    def __init__(self, model: Model, model_config: ModelConfig):
        self.model = model
        self.model_config = model_config
        print(
            f"{self.model_config.name} runner initialized...                                       ",
            end="\r",
        )

    def generate_permutations(self, n: int, s: str) -> List[str]:
        max_permutations = math.factorial(len(s))
        if n > max_permutations:
            raise ValueError(
                f"Cannot generate more than {max_permutations} unique permutations for the string '{s}'"
            )
        permutations = set()
        while len(permutations) < n:
            perm = "".join(random.sample(s, len(s)))
            permutations.add(perm)

        return list(permutations)

    def spread_or_sample(self, arr: List[str], size: int) -> List[str]:
        """
        Expands or samples the input array to the specified size.
        If the array is smaller than the specified size, it repeats elements until the size is reached.
        If the array is larger than the specified size, it returns a random sample of the array.
        """
        if len(arr) < size:
            # Repeat elements to reach the desired size
            repeated = (arr * (size // len(arr) + 1))[:size]
            return repeated
        else:
            # Randomly sample elements if the array is larger than the desired size
            return random.sample(arr, size)

    def run(self):
        for size in self.model_config.token_lengths:
            print(
                f"{self.model_config.name} @ {size} initializing...                                       ",
                end="\r",
            )
            fit_string = self.model.generate_string_of_token_length(size).string
            print(
                f"Building permutations...                                       ",
                end="\r",
            )
            permutations = self.generate_permutations(
                (
                    self.model_config.runs
                    if self.model_config.runs < self.model_config.permutations
                    else self.model_config.permutations
                ),
                fit_string,
            )
            batch_text = self.spread_or_sample(permutations, self.model_config.runs)
            print("                                       ", end="\r")
            print(f"\n{self.model_config.name} @ {size} tokens:")
            batch_results = batch_timer(
                self.model.embed, self.model_config.runs, batch_text
            )
            print(
                f"""Average: {batch_results.average:.4f} seconds                                       
Maximum: {batch_results.maximum:.4f} seconds                                       
Minimum: {batch_results.minimum:.4f} seconds                                       
Device: {self.model.device}                                       
Total Runs: {self.model_config.runs}                                       
"""
            )

    def data_run(self) -> list[RunStat]:
        total_runs = []
        for size in self.model_config.token_lengths:
            size_runs = []
            print(
                f"{self.model_config.name} @ {size} initializing...                                       ",
                end="\r",
            )
            fit_string = self.model.generate_string_of_token_length(size).string
            print(
                f"Building permutations...                                       ",
                end="\r",
            )
            permutations = self.generate_permutations(
                (
                    self.model_config.runs
                    if self.model_config.runs < self.model_config.permutations
                    else self.model_config.permutations
                ),
                fit_string,
            )
            batch_text = self.spread_or_sample(permutations, self.model_config.runs)
            print("                                       ", end="\r")
            print(f"\n{self.model_config.name} @ {size} tokens executing...")

            for run_index in range(len(batch_text)):
                print(f"Batch {run_index}/{len(batch_text)}", end="\r")
                runstats: list[RunStat] = self.model.embed_timed(
                    [batch_text[run_index]], self.model_config, size
                )
                size_runs.extend(runstats)
                total_runs.extend(runstats)
            run_stats_dicts = [asdict(stat) for stat in size_runs]
            current_datetime_str = date_string(datetime.now())
            filename = f"run_____{self.model_config.name.split('/')[len(self.model_config.name.split('/'))-1]}_____{size}_____{self.model_config.runs}_____{self.model_config.permutations}_____{current_datetime_str}.json"
            with open(filename, "w") as f:
                json.dump(run_stats_dicts, f, default=str, indent=4)
        return total_runs
