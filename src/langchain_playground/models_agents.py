from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen3:1.7b",
    temperature=0,
)

response = model.invoke("what is the capital of France?")

print(response.content)
