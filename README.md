---
title: Assignment AI_Infiheal
emoji: 🏃
sdk: docker
pinned: false
---
# AI Infiheal Assignment

This repository contains the code for the AI Infiheal assignment, which involves creating a FastAPI server with endpoints for Retrieval-Augmented Generation (RAG) and classification tasks using open-source Large Language Models (LLMs). The project also includes optimizing response times, creating a Hugging Face Space, and containerizing the application using Docker.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/ai_infiheal_assignment.git
    cd ai_infiheal_assignment
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set up the required environment variables (see [Environment Variables](#environment-variables)).

2. Start the FastAPI server:

    ```bash
    uvicorn app:app --host 0.0.0.0 --port 8000
    ```

3. Access the API documentation at `http://localhost:8000/docs`.

## Endpoints

### Retrieval-Augmented Generation (RAG)

- **POST** `/rag` - Generate a response based on the input query using RAG.

    Request body:
    ```json
    {
        "query": "Your input query here"
    }
    ```

    Response:
    ```json
    {
        "response": "Generated response based on the query"
    }
    ```

### Classification

- **POST** `/classify` - Classify the input text.

    Request body:
    ```json
    {
        "text": "Text to classify"
    }
    ```

    Response:
    ```json
    {
        "label": "Predicted label"
    }
    ```

## Environment Variables

- `TRANSFORMERS_CACHE` - Path to the cache directory for transformers models. Default is `/tmp/cache`.

Example:
```bash
export TRANSFORMERS_CACHE=/tmp/cache

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
