from dataclasses import dataclass


@dataclass
class ModelConfig:
    name: str
    token_lengths: list[int]
    permutations: int
    runs: int
