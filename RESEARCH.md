# Embedding model market analysis

This is an analysis of open source embedding models in the market today. The models selected are ones that have minimal EULA restrictions, high scores on the MTEB, and moderate dimensionality/max-sequence-length.

## Models

| **Model**                                                                                                 | **MTEB Ranking** | **Parameters** | **Dimensions** | **Max Tokens** |
| --------------------------------------------------------------------------------------------------------- | ---------------- | -------------- | -------------- | -------------- |
| [BAAI/bge-en-icl](https://huggingface.co/BAAI/bge-en-icl)                                                 | 4                | 7.111B         | 4096           | 32,768         |
| [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5)                                   | 47               | 335M           | 1024           | 512            |
| [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5)                                     | 55               | 109M           | 768            | 512            |
| [Alibaba-NLP/gte-Qwen2-7B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct)             | 7                | 7.611B         | 3584           | 131,072        |
| [Alibaba-NLP/gte-Qwen2-1.5B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen2-1.5B-instruct)         | 17               | 1.776B         | 1536           | 131,072        |
| [Alibaba-NLP/gte-large-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5)                     | 29               | 434M           | 1024           | 8,192          |
| [Alibaba-NLP/gte-base-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-base-en-v1.5)                       | 51               | 137M           | 768            | 8,192          |
| [sentence-transformers/all-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2) | 149              | 33M            | 384            | 512            |

### Open AI Reference Point

For comparison to Open AI rankings:

| **Model**                            | **MTEB Ranking** | **Parameters** | **Dimensions** | **Max Tokens** |
| ------------------------------------ | ---------------- | -------------- | -------------- | -------------- |
| **Text-embedding-3-large**           | 39               | N/A            | 3072           | 8191           |
| **Text-embedding-3-small**           | 69               | N/A            | 1536           | 8191           |
| **Text-embedding-ada-002**           | 91               | N/A            | 1536           | 8191           |
| **Text-embedding-ada-002v2 (Azure)** | N/A              | N/A            | N/A            | 8191           |

## Instance Types

These are the instance types that are capable of running these models. There are others, but these provide a good range of cost.

Deep Learning OSS Nvidia Driver AMI GPU PyTorch 2.5 (Ubuntu 22.04) - ami-00dddcf8fefea182f (64-bit (x86)) / ami-0ed05a5c0d640bb4b (64-bit (Arm))

| Instance Type | GPU Memory (GB) | CPU | RAM (GB) | On-Demand Price per Hour (USD) | Cost per Month (USD) | Cost per Year (USD) |
| ------------- | --------------- | --- | -------- | ------------------------------ | -------------------- | ------------------- |
| g6.2xlarge    | 24              | 8   | 32       | $0.9776                        | $703.87              | $8,563.78           |
| g6e.xlarge    | 48              | 4   | 32       | $1.861                         | $1,339.92            | $16,302.36          |
| g6e.2xlarge   | 48              | 8   | 64       | $2.24208                       | $1,614.30            | $19,640.62          |
| g4dn.12xlarge | 64              | 48  | 192      | $3.912                         | $2,816.64            | $34,269.12          |
| g6.12xlarge   | 96              | 48  | 192      | $4.6016                        | $3,313.15            | $40,310.02          |

## Projected Cloud Cost

Cost to host each model on these instances shown below - this is strictly estimated adequacy based on experiment outcomes comparing several model parameters/sequence length requirements.

| **Model**                                                                                                 | **MTEB Rank** | **Parameters** | **Instance GPU (GB)** | **g6.12xlarge** ($/Month/Year) | **g4dn.12xlarge** ($/Month/Year) | **g6e.2xlarge** ($/Month/Year) | **g6e.xlarge** ($/Month/Year) | **g6.2xlarge** ($/Month/Year) |
| --------------------------------------------------------------------------------------------------------- | ------------: | -------------: | --------------------- | ------------------------------ | -------------------------------- | ------------------------------ | ----------------------------- | ----------------------------- |
| [BAAI/bge-en-icl](https://huggingface.co/BAAI/bge-en-icl)                                                 |             4 |         7.111B | 96                    | $3,313 / $40,310               | $2,816 / $34,269                 | -                              | -                             | -                             |
| [Alibaba-NLP/gte-Qwen2-7B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct)             |             7 |         7.611B | 96                    | $3,313 / $40,310               | $2,816 / $34,269                 | -                              | -                             | -                             |
| [Alibaba-NLP/gte-Qwen2-1.5B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen2-1.5B-instruct)         |            17 |         1.776B | 48                    | $3,313 / $40,310               | $2,816 / $34,269                 | $1,614 / $19,640               | $1,339 / $16,302              | -                             |
| [Alibaba-NLP/gte-large-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5)                     |            29 |           434M | 48                    | $3,313 / $40,310               | $2,816 / $34,269                 | $1,614 / $19,640               | $1,339 / $16,302              | $703.87 / $8,563              |
| [Alibaba-NLP/gte-base-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-base-en-v1.5)                       |            51 |           137M | 48                    | $3,313 / $40,310               | $2,816 / $34,269                 | $1,614 / $19,640               | $1,339 / $16,302              | $703.87 / $8,563              |
| [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5)                                   |            47 |           335M | 24                    | $3,313 / $40,310               | $2,816 / $34,269                 | $1,614 / $19,640               | $1,339 / $16,302              | $703.87 / $8,563              |
| [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5)                                     |            55 |           109M | 24                    | $3,313 / $40,310               | $2,816 / $34,269                 | $1,614 / $19,640               | $1,339 / $16,302              | $703.87 / $8,563              |
| [sentence-transformers/all-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2) |           149 |            33M | 24                    | $3,313 / $40,310               | $2,816 / $34,269                 | $1,614 / $19,640               | $1,339 / $16,302              | $703.87 / $8,563              |

<br></br>

# Model dispositions

### Best in class model - [BAAI/bge-en-icl](https://huggingface.co/BAAI/bge-en-icl)

This model sits at #4 in the MTEB and has 7.1B parameters. It also has a very deep dimensionality of 4096. The innovation in this model is called "In Context Learning", which allows you to send the model `{instruct, query, response}` to prompt different behavior of the model. I feel this can have very big implications for both:

- Disambiguating terms that are lexically similar but semantically different (ie: river "bank" / finanical "bank" , "ruler" instrument / "ruler" of country)
- Targeting towards personalized or context specific embedding spaces. Can largely alter sortings/rankings, seen as similar to `bq` in technologies like SOLR (Apache Lucene)

---

### Above average model - [Alibaba-NLP/gte-Qwen2-1.5B-instruct](https://huggingface.co/Alibaba-NLP/gte-Qwen2-1.5B-instruct)

This model has 1.776B parameters, which deliver high quality embeddings (#17 on the MTEB). It does require higher resources/cost, but can be mitigated by capping the sequence length to a lower maximum (ie: `8192`).

This model also has the same dimensionality as Open AI's ada-002 model. This presents an easy migration strategy for those currently on that model.

---

### Noteworthy model - [Alibaba-NLP/gte-large-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5)

This model has 434M parameters, so its likely to run in lower cost environments. It also has a 8192 max sequence length, giving it the ability to handle a wide variety of use cases. The dimensionality falls a little bit short of the other high ranking models. This model is #29 on the MTEB leaderboard as of 1/12/2025, which is above all of Open AI's current offerings.

---

### Small sequence, small hardware models - [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5) and [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5)

I think both the models are limited because of their `512 max sequence limitation`, but for smaller usecases you can get a decent amount of juice for the squeeze cost wise.

---

### The POC model - [sentence-transformers/all-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2)

For ~90% less parameters than the [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5) (#45), you can retain quite a bit of rank (#149). This model can run on most basic laptops today on CPU.

---

<br></br>

# Experiment Results

This project is ready to run on any hardware spun up - AWS has service quotas on GPU instances, once those are approved I'll publish instance specific results. For the time being this was run locally with the below configuration:

### Cost

Consider the cost of hardware to be `~$8000`

Assume the average lifespan of the hardware in a typical data center to be at max `3-5 years`.

These performances can be acheieved for `$1600-$2,600 per year`.

### Hardware

- GPU - `NVIDIA 4090 (Gigabyte GeForce RTX 4090 Gaming OC 24G Graphics Card)`
- CPU - `32 Core - 64 -Thread - 4GHz Frequency (Ryzen Threadripper 7970x)`
- RAM - `128GB DDR5-6400 (G.SKILL Zeta R5 Neo 32GB x 4)`

### Results

| Model                               | Sequence Length | Avg Time (s) | Max Time (s) | Min Time (s) | Device | Total Runs | Tokens/Minute |
| :---------------------------------- | --------------: | -----------: | -----------: | -----------: | :----- | ---------: | ------------: |
| BAAI/bge-large-en-v1.5              |              10 |       0.2198 |       0.5346 |       0.2116 | cuda   |         50 |       2729.75 |
| BAAI/bge-large-en-v1.5              |             100 |       0.2418 |       0.5427 |       0.2347 | cuda   |         50 |      24813.90 |
| BAAI/bge-large-en-v1.5              |             250 |       0.3500 |       0.6408 |       0.3425 | cuda   |         50 |      42857.10 |
| BAAI/bge-large-en-v1.5              |             500 |       0.7059 |       1.0895 |       0.6574 | cuda   |         50 |      42498.90 |
| BAAI/bge-base-en-v1.5               |              10 |       0.1301 |       0.4362 |       0.1223 | cuda   |         50 |       4611.84 |
| BAAI/bge-base-en-v1.5               |             100 |       0.1359 |       0.4573 |       0.1259 | cuda   |         50 |      44150.10 |
| BAAI/bge-base-en-v1.5               |             250 |       0.1538 |       0.4680 |       0.1352 | cuda   |         50 |      97529.30 |
| BAAI/bge-base-en-v1.5               |             500 |       0.2390 |       0.5599 |       0.2175 | cuda   |         50 |     125523.00 |
| Alibaba-NLP/gte-Qwen2-1.5B-instruct |             100 |       0.7124 |       1.0462 |       0.7031 | cuda   |         50 |       8422.23 |
| Alibaba-NLP/gte-Qwen2-1.5B-instruct |             500 |       2.2133 |       2.4899 |       2.2006 | cuda   |         50 |      13554.40 |
| Alibaba-NLP/gte-Qwen2-1.5B-instruct |            1000 |       4.2727 |       4.6429 |       4.2241 | cuda   |         50 |      14042.60 |
| Alibaba-NLP/gte-large-en-v1.5       |             100 |       0.3048 |       0.6040 |       0.2975 | cuda   |         50 |      19685.00 |
| Alibaba-NLP/gte-large-en-v1.5       |             500 |       0.7731 |       1.0693 |       0.7654 | cuda   |         50 |      38804.80 |
| Alibaba-NLP/gte-large-en-v1.5       |            1000 |       1.4105 |       1.6820 |       1.4001 | cuda   |         50 |      42538.10 |
| Alibaba-NLP/gte-base-en-v1.5        |             100 |       0.1705 |       0.4763 |       0.1607 | cuda   |         50 |      35190.60 |
| Alibaba-NLP/gte-base-en-v1.5        |             500 |       0.2780 |       0.5712 |       0.2652 | cuda   |         50 |     107914.00 |
| Alibaba-NLP/gte-base-en-v1.5        |            1000 |       0.5433 |       0.7942 |       0.4945 | cuda   |         50 |     110436.00 |
| Alibaba-NLP/gte-base-en-v1.5        |            2500 |       1.4888 |       1.7312 |       1.4515 | cuda   |         50 |     100752.00 |

<br></br>

# Insights

### **1. Performance variability suggests model stability at higher sequence lengths**

For lower sequence lengths (e.g., **10 to 100 tokens**), there is high variability in tokenization and inference time. This was shown to stabilize at higher sequence lengths (500+).

### **2. Linear growth in latency with longer sequence lengths**

Latency scales linearly with sequence length, particularly for **Alibaba-NLP/gte-Qwen2-1.5B-instruct**, where processing 500 tokens takes 2.2 seconds and 1000 tokens takes 4.3 seconds, representing a ~2x increase in time.

### **3. 24GB GPU produces decent tokens per minute rate for [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5)**

The highest token processing rate was executed by [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5) with **125K tokens/minute** at **500 sequence length**. This is at the upper bounds of this model's max sequence length, indicating a high stress speed that is adequate for decent volume.

Assuming a correlation in performance with other models that have near **137M parameters**, this may be an adequate GPU for certain use cases.

### **4. Significant savings purchasing hardware for on-premise deployment**

The costs seem to be very inflated for GPU instances on AWS. With cost of electricity considered, you can look at around a `2x savings` when you purchase and deploy the hardware yourself.

<br></br>
<br></br>
<br></br>

# G6.12X LARGE TESTING

      96 GB GPU
      48 CPU
      192 GB MEMORY

## Alibaba-NLP/gte-Qwen2-1.5B-instruct

Based off of 100 runs.

- Performance peak at 1K tokens

| Sequence Length | Total Tokens Processed | Total Completion Time | Tokens Per Second |
| --------------- | ---------------------- | --------------------- | ----------------- |
| 100.0           | 10000.0                | 5.0511                | ~1979             |
| 250.0           | 25000.0                | 9.3451                | ~2675             |
| 1000.0          | 100000.0               | 32.0715               | ~3188             |
| 2500.0          | 250000.0               | 98.8960               | ~2527             |
| 5000.0          | 500000.0               | 201.7642              | ~2478             |
| 7500.0          | 750000.0               | 319.8190              | ~2345             |

| Stage      | Total Tokens | Total Completion Time | Tokens Per Second |
| ---------- | ------------ | --------------------- | ----------------- |
| Inference  | 1625000      | 78.5158               | 2096.47           |
| Tokenizing | 1625000      | 588.4311              | 2761.58           |

---

## BAAI/bge-base-en-v1.5

Based off of 100 runs.

| Sequence Length | Total Tokens Processed | Total Completion Time | Tokens Per Second |
| --------------- | ---------------------- | --------------------- | ----------------- |
| 100.0           | 10000.0                | 0.5502                | ~18175            |
| 250.0           | 25000.0                | 0.7323                | ~34139            |
| 500.0           | 50000.0                | 1.2030                | ~41562            |

| Stage      | Total Tokens | Total Completion Time | Tokens Per Second |
| ---------- | ------------ | --------------------- | ----------------- |
| Inference  | 85000        | 1.5685                | 54191             |
| Tokenizing | 85000        | 0.9170                | 92693             |

---

## BAAI/bge-large-en-v1.5

Based off of 100 runs.

| Sequence Length | Total Tokens Processed | Total Completion Time | Tokens Per Second |
| --------------- | ---------------------- | --------------------- | ----------------- |
| 100.0           | 10000.0                | 1.4558                | ~6869             |
| 250.0           | 25000.0                | 2.1860                | ~11436            |
| 500.0           | 50000.0                | 4.0974                | ~12202            |

| Stage      | Total Tokens | Total Completion Time | Tokens Per Second |
| ---------- | ------------ | --------------------- | ----------------- |
| Inference  | 85000        | 3.1650                | 26856             |
| Tokenizing | 85000        | 4.5744                | 18581             |

---

## Alibaba-NLP/gte-base-en-v1.5

Based off of 100 runs.

| Sequence Length | Total Tokens Processed | Total Completion Time | Tokens Per Second |
| --------------- | ---------------------- | --------------------- | ----------------- |
| 100.0           | 10000.0                | 0.6889                | ~14515            |
| 250.0           | 25000.0                | 0.9021                | ~27713            |
| 500.0           | 50000.0                | 1.9039                | ~26261            |
| 1000.0          | 100000.0               | 4.1895                | ~23869            |
| 2500.0          | 250000.0               | 12.8993               | ~19380            |
| 5000.0          | 500000.0               | 31.4449               | ~15900            |
| 7500.0          | 750000.0               | 56.2406               | ~13335            |

| Stage      | Total Tokens | Total Completion Time | Tokens Per Second |
| ---------- | ------------ | --------------------- | ----------------- |
| Inference  | 1685000      | 4.7566                | 354244            |
| Tokenizing | 1685000      | 103.5126              | 16278             |

---

## Alibaba-NLP/gte-large-en-v1.5

Based off of 100 runs.

| Sequence Length | Total Tokens Processed | Total Completion Time | Tokens Per Second |
| --------------- | ---------------------- | --------------------- | ----------------- |
| 100.0           | 10000.0                | 1.7193                | ~5816             |
| 250.0           | 25000.0                | 3.7472                | ~66716            |
| 500.0           | 50000.0                | 6.2924                | ~7946             |
| 1000.0          | 100000.0               | 12.3111               | ~8122             |
| 2500.0          | 250000.0               | 38.6131               | ~6474             |
| 5000.0          | 500000.0               | 94.2031               | ~5307             |
| 7500.0          | 750000.0               | 168.7148              | ~4445             |

| Stage      | Total Tokens | Total Completion Time | Tokens Per Second |
| ---------- | ------------ | --------------------- | ----------------- |
| Inference  | 1685000      | 9.3177                | ~180838           |
| Tokenizing | 1685000      | 316.2833              | ~5327             |

---

## sentence-transformers/all-MiniLM-L12-v1

Based off of 100 runs.

| Sequence Length | Total Tokens Processed | Total Completion Time | Tokens Per Second |
| --------------- | ---------------------- | --------------------- | ----------------- |
| 100.0           | 10000.0                | 0.5539                | ~18053            |
| 250.0           | 25000.0                | 0.5520                | ~45289            |
| 500.0           | 50000.0                | 0.6064                | ~82453            |

| Stage      | Total Tokens | Total Completion Time | Tokens Per Second |
| ---------- | ------------ | --------------------- | ----------------- |
| Inference  | 85000        | 1.5566                | ~54606            |
| Tokenizing | 85000        | 0.1557                | ~545921           |
