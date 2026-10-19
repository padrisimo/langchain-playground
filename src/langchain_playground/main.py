from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_playground.photo_decoder import build_image_message, choose_image_file
from langchain_playground.prompt import CHEF_PROMPT, SYSTEM_CHEF_PROMPT
from langchain_playground.tools import web_search

agent = create_agent(
    model="ollama:qwen3:1.7b", tools=[web_search], system_prompt=SYSTEM_CHEF_PROMPT
)

response = agent.invoke({"messages": [HumanMessage(content="hello how are you?")]})

path = choose_image_file()
message = build_image_message(path, CHEF_PROMPT)

print(response["messages"][-1].content)
