# Use Python 3.10.12 as the base image
FROM python:3.10.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "cli", "--name", "BAAI/bge-large-en-v1.5"]