# AI Model Load Tester

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
