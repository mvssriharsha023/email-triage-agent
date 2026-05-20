from langchain_ollama import ChatOllama

__all__ = ["llm"]

llm = ChatOllama(
    model="mistral",
    temperature=0.2
)