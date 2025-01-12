#!/bin/bash

set +e # Disable script exit on error

./cli --name BAAI/bge-large-en-v1.5 --tokens 500 --runs 100 --permutations 100  --output true
./cli --name Alibaba-NLP/gte-Qwen2-1.5B-instruct --tokens 50 --runs 100 --permutations 100  --output true
