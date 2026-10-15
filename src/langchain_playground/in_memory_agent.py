from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(model="ollama:qwen3:1.7b", checkpointer=InMemorySaver())
config = {"configurable": {"thread_id": "1"}}

response = agent.invoke(
    {
        "messages": [
            HumanMessage(content="My favourite color is green."),
        ]
    },
    config,
)
print(response["messages"][-1].content)
print("--------------------------------------------------")

response = agent.invoke(
    {
        "messages": [
            HumanMessage(content="what is my favourite color?"),
        ]
    },
    config,
)

print(response["messages"][-1].content)
