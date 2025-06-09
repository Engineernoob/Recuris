# core/llm.py
from ollama import chat

def query_llama(prompt: str, model: str = "gemma2:2b") -> str:
    response = chat(model=model, messages=[
        {"role": "user", "content": prompt}
    ])
    return response["message"]["content"]