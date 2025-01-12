#!/bin/bash

set +e # Disable script exit on error

# model runs
# echo "Unique model runs"

./cli --name BAAI/bge-large-en-v1.5 --tokens 10 --runs 50 --permutations 50
./cli --name BAAI/bge-large-en-v1.5 --tokens 100 --runs 50 --permutations 50
./cli --name BAAI/bge-large-en-v1.5 --tokens 250 --runs 50 --permutations 50
./cli --name BAAI/bge-large-en-v1.5 --tokens 500 --runs 50 --permutations 50

./cli --name BAAI/bge-base-en-v1.5 --tokens 10 --runs 50 --permutations 50
./cli --name BAAI/bge-base-en-v1.5 --tokens 100 --runs 50 --permutations 50
./cli --name BAAI/bge-base-en-v1.5 --tokens 250 --runs 50 --permutations 50
./cli --name BAAI/bge-base-en-v1.5 --tokens 500 --runs 50 --permutations 50

./cli --name Alibaba-NLP/gte-Qwen2-1.5B-instruct --tokens 100 --runs 50 --permutations 50
./cli --name Alibaba-NLP/gte-Qwen2-1.5B-instruct --tokens 500 --runs 50 --permutations 50
./cli --name Alibaba-NLP/gte-Qwen2-1.5B-instruct --tokens 1000 --runs 50 --permutations 50

./cli --name Alibaba-NLP/gte-large-en-v1.5 --tokens 100 --runs 50 --permutations 50
./cli --name Alibaba-NLP/gte-large-en-v1.5 --tokens 500 --runs 50 --permutations 50
./cli --name Alibaba-NLP/gte-large-en-v1.5 --tokens 1000 --runs 50 --permutations 50

./cli --name Alibaba-NLP/gte-base-en-v1.5 --tokens 100 --runs 50 --permutations 50
./cli --name Alibaba-NLP/gte-base-en-v1.5 --tokens 500 --runs 50 --permutations 50
./cli --name Alibaba-NLP/gte-base-en-v1.5 --tokens 1000 --runs 50 --permutations 50
./cli --name Alibaba-NLP/gte-base-en-v1.5 --tokens 2500 --runs 50 --permutations 50



# echo "20% input overlap”"

# ./cli --name BAAI/bge-large-en-v1.5 --tokens 10 --runs 50 --permutations 10
# ./cli --name BAAI/bge-large-en-v1.5 --tokens 100 --runs 50 --permutations 10
# ./cli --name BAAI/bge-large-en-v1.5 --tokens 250 --runs 50 --permutations 10
# ./cli --name BAAI/bge-large-en-v1.5 --tokens 500 --runs 50 --permutations 10

# ./cli --name BAAI/bge-base-en-v1.5 --tokens 10 --runs 50 --permutations 10
# ./cli --name BAAI/bge-base-en-v1.5 --tokens 100 --runs 50 --permutations 10
# ./cli --name BAAI/bge-base-en-v1.5 --tokens 250 --runs 50 --permutations 10
# ./cli --name BAAI/bge-base-en-v1.5 --tokens 500 --runs 50 --permutations 10

# ./cli --name Alibaba-NLP/gte-Qwen2-1.5B-instruct --tokens 100 --runs 50 --permutations 10
# ./cli --name Alibaba-NLP/gte-Qwen2-1.5B-instruct --tokens 500 --runs 50 --permutations 10
# ./cli --name Alibaba-NLP/gte-Qwen2-1.5B-instruct --tokens 1000 --runs 50 --permutations 10

# ./cli --name Alibaba-NLP/gte-large-en-v1.5 --tokens 100 --runs 50 --permutations 10
# ./cli --name Alibaba-NLP/gte-large-en-v1.5 --tokens 500 --runs 50 --permutations 10
# ./cli --name Alibaba-NLP/gte-large-en-v1.5 --tokens 1000 --runs 50 --permutations 10

# ./cli --name Alibaba-NLP/gte-base-en-v1.5 --tokens 100 --runs 50 --permutations 10
# ./cli --name Alibaba-NLP/gte-base-en-v1.5 --tokens 500 --runs 50 --permutations 10
# ./cli --name Alibaba-NLP/gte-base-en-v1.5 --tokens 1000 --runs 50 --permutations 10
# ./cli --name Alibaba-NLP/gte-base-en-v1.5 --tokens 2500 --runs 50 --permutations 10













# ./cli --name BAAI/bge-base-en-v1.5
# ./cli --name Alibaba-NLP/gte-Qwen2-1.5B-instruct
# ./cli --name Alibaba-NLP/gte-large-en-v1.5
# ./cli --name Alibaba-NLP/gte-base-en-v1.5