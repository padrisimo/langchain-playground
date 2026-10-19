from pathlib import Path
from langchain_ollama import ChatOllama
from langchain_playground.photo_decoder import build_image_message, choose_image_file
from langchain_playground.tools import web_search
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

vision_llm = ChatOllama(
    model="qwen2.5vl:3b", temperature=0, num_ctx=8192, keep_alive="10m"
)
tool_llm = ChatOllama(model="qwen3:1.7b", temperature=0, num_ctx=8192, keep_alive="10m")

path = choose_image_file()
msg = build_image_message(
    Path(path),
    "List only the food ingredients you see, comma separated, no explanation.",
)

logging.info("identifying ingredients...")
ingredients = vision_llm.invoke([msg]).content.strip()
logging.info("ingredients: %s", ingredients)

logging.info("searching recipe...")
search_results = web_search.invoke(f"recipe with {ingredients}")

logging.info("summarizing recipe...")
recipe = tool_llm.invoke(
    [
        ("system", "You are a chef. Summarize the recipe in clear, concise steps."),
        ("human", f"Ingredients: {ingredients}\nSearch results:\n{search_results}"),
    ]
).content

print(recipe)
