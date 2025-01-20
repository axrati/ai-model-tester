#!/usr/bin/env python3
from lib.model import Model
from lib.model_config import ModelConfig
from lib.model_runner import ModelRunner
from dataclasses import asdict
from datetime import datetime
import json

models: list[ModelConfig] = [
    ModelConfig(
        name="BAAI/bge-en-icl",
        token_lengths=[100, 1000, 5000, 10000, 30000],
        permutations=100,
        runs=100,
    ),
    ModelConfig(
        name="BAAI/bge-large-en-v1.5",
        token_lengths=[100, 200, 500],
        permutations=100,
        runs=100,
    ),
    ModelConfig(
        name="BAAI/bge-base-en-v1.5",
        token_lengths=[100, 200, 500],
        permutations=100,
        runs=100,
    ),
    ModelConfig(
        name="Alibaba-NLP/gte-Qwen2-7B-instruct",
        token_lengths=[100, 1000, 5000, 10000, 50000, 130000],
        permutations=100,
        runs=100,
    ),
    ModelConfig(
        name="Alibaba-NLP/gte-Qwen2-1.5B-instruct",
        token_lengths=[
            100,
            500,
            1000,
        ],
        permutations=100,
        runs=100,
    ),
    ModelConfig(
        name="Alibaba-NLP/gte-large-en-v1.5",
        token_lengths=[100, 200, 500, 1000, 5000, 8000],
        permutations=100,
        runs=100,
    ),
    ModelConfig(
        name="Alibaba-NLP/gte-base-en-v1.5",
        token_lengths=[100, 200, 500, 1000, 5000, 8000],
        permutations=100,
        runs=100,
    ),
    ModelConfig(
        name="sentence-transformers/all-MiniLM-L12-v1",
        token_lengths=[100, 200, 500],
        permutations=100,
        runs=100,
    ),
]


outputs = []
for mc in models:
    try:
        outputs = []
        model = Model(mc)
        runner = ModelRunner(model=model, model_config=mc)
        data = runner.data_run()

    except:
        print(f"Error running model: {mc.name}")
        print("")
        print("Trying next...\n")
        continue

# run_stats_dicts = [asdict(stat) for stat in outputs]

# current_datetime_str = datetime.now().strftime("%Y%m%d_%H%M%S")
# filename = f"run_stats_{current_datetime_str}.json"
# with open(filename, "w") as f:
#     json.dump(run_stats_dicts, f, default=str, indent=4)
