from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_playground.photo_decoder import build_image_message, choose_image_file
from langchain_playground.prompt import CHEF_PROMPT, SYSTEM_CHEF_PROMPT
from langchain_playground.tools import web_search
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logging.info("creating our agent...")
agent = create_agent(
    model="ollama:qwen3-vl:2b", tools=[web_search], system_prompt=SYSTEM_CHEF_PROMPT
)


logging.info("choosing our image...")
path = choose_image_file()
message = build_image_message(path, CHEF_PROMPT)

logging.info("invoking our agent...")
response = agent.invoke(
    {"messages": [message]}
)


print(response["messages"][-1].content)