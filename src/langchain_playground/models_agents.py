from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage

model = init_chat_model(model="ollama:qwen3:1.7b", temperature=0)

agent = create_agent(model=model)

response = agent.invoke(
    {"messages": [HumanMessage(content="Write a short poem about the ocean.")]}
)

print(response["messages"][-1].content)
