# AI Model Tester

Purpose of this repository is to be able to pull/run models against different input sizes to gauge feasibility in different hardware environments.

For HuggingFace models - just copy the model name over. For example: `BAAI/bge-large-en-v1.5`

Use `--fetch https:link/to/model.zip` and `--local true` to load models from sources outside of HuggingFace.

## Running Models

Install dependencies with `pip install -r requirements.txt`.

The `./cli` function will print stats from the run for you to view. To save outputs, use `--output true`

```bash
# Local
./cli --name BAAI/bge-large-en-v1.5
```

## Arguments

| **Argument**     | **Type** | **Default** | **Required** | **Description**                                                                                                                                  |
| ---------------- | -------- | ----------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--name`         | `str`    | N/A         | Yes          | The name of the model to process.                                                                                                                |
| `--tokens`       | `int`    | `100`       | No           | The number of tokens to generate or process.                                                                                                     |
| `--runs`         | `int`    | `3`         | No           | The number of runs to execute the model with the specified configurations.                                                                       |
| `--permutations` | `int`    | `3`         | No           | The number of permutations to generate for each token length - shouldnt be larger than `--runs`.                                                 |
| `--device`       | `str`    | `"auto"`    | No           | Specifies the device to run the model on. Options: `"auto"`, `"cpu"`, `"cuda"`.                                                                  |
| `--fetch`        | `str`    | N/A         | No           | A URL pointing to a zip file. Zip file is downloaded and extracted to the current directory. Used for models externally sourced from HuggingFace |
| `--local`        | `bool`   | `False`     | No           | Forces the model to look locally in the current directory for a folder named `--name` and load its model contents.                               |
| `--output`       | `bool`   | `False`     | No           | Outputs the run data to a json file in the current directory                                                                                     |

## Library

```python
from lib.model import Model
from lib.model_config import ModelConfig
from lib.model_runner import ModelRunner

config = ModelConfig(
    name="BAAI/bge-large-en-v1.5",
    token_lengths=[100, 200, 500],
    permutations=100,
    runs=100,
)

model = Model(config)
runner = ModelRunner(model=model, model_config=config)

runner.run() # Print to console
data = runner.data_run() # Returns data
```

# Research

## Parameters

These are the model names that I used here.

| **Model**                                                                                         | **MTEB Ranking** | **Parameters** | **Dimensions** | **Max Tokens** |
| ------------------------------------------------------------------------------------------------- | ---------------- | -------------- | -------------- | -------------- |
| [BAAI/bge-en-icl](https://huggingface.co/BAAI/bge-en-icl)                                         | 4                | 7.111B         | 4096           | 32,768         |
| [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5)                           | 47               | 335M           | 1024           | 512            |
| [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5)                             | 55               | 109M           | 768            | 512            |
| [Alibaba-NLP/gte-Qwen2-7B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct)     | 7                | 7.611B         | 3584           | 131,072        |
| [Alibaba-NLP/gte-Qwen2-1.5B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen2-1.5B-instruct) | 17               | 1.776B         | 1536           | 131,072        |
| [Alibaba-NLP/gte-large-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5)             | 29               | 434M           | 1024           | 8,192          |
| [Alibaba-NLP/gte-base-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-base-en-v1.5)               | 51               | 137M           | 768            | 8,192          |

#### Open AI Reference Point

| **Model**                    | **MTEB Ranking** | **Parameters** | **Dimensions** | **Max Tokens** |
| ---------------------------- | ---------------- | -------------- | -------------- | -------------- |
| **Text-embedding-3-large**   | 39               | N/A            | 3072           | N/A            |
| **Text-embedding-3-small**   | 69               | N/A            | 1536           | 8191           |
| **Text-embedding-ada-002**   | 91               | N/A            | 1536           | 8191           |
| **Text-embedding-ada-002v2** | N/A              | N/A            | N/A            | 8191           |

#### Instance Types

Deep Learning OSS Nvidia Driver AMI GPU PyTorch 2.5 (Ubuntu 22.04) - ami-00dddcf8fefea182f (64-bit (x86)) / ami-0ed05a5c0d640bb4b (64-bit (Arm))

| Instance Type | GPU Memory (GB) | CPU | RAM (GB) | On-Demand Price per Hour (USD) |
| ------------- | --------------- | --- | -------- | ------------------------------ |
| g6.2xlarge    | 24              | 8   | 32       | $0.9776                        |
| g6e.xlarge    | 48              | 4   | 32       | $1.861                         |
| g6e.2xlarge   | 48              | 8   | 64       | $2.24208                       |
| g4dn.12xlarge | 64              | 48  | 192      | $3.912                         |
| g6.12xlarge   | 96              | 48  | 192      | $4.6016                        |

## Implementation

The goal here is to test out how different models perform on different architecture.

Some models will not be applied to certain instance types because they dont have the resources to run them.

Testing was also done via the `./cli` interface to make sure long times were avoided. Acceptable response time is likely maxed at 2-3 seconds for high throughput needs.

All of the run tests will be found here.
