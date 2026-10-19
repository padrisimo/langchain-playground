# LangChain Playground

Vision + web search recipe finder using local Ollama models.

## How it works

Two models, no agent framework:
1. **qwen2.5vl:3b** (vision) — looks at the image, lists food ingredients
2. **qwen3:1.7b** (tools) — searches the web via DuckDuckGo, summarizes a recipe

## Prerequisites

```bash
# Install models
ollama pull qwen2.5vl:3b
ollama pull qwen3:1.7b

# Python deps
uv sync
```

## Run

```bash
python3 src/langchain_playground/main.py
```

A file picker opens → choose an image → prints a recipe.

## Models

| Model | Size | Capabilities |
|-------|------|--------------|
| qwen2.5vl:3b | 3.2 GB | vision, completion |
| qwen3:1.7b | 1.4 GB | tools, thinking, completion |

## Project structure

```
src/langchain_playground/
├── main.py           # entry point (31 lines)
├── photo_decoder.py  # file picker + image resize + base64
└── tools.py          # web_search wrapper (DuckDuckGo)
```

## Requirements

- macOS/Linux (tkinter for file picker)
- Ollama running locally
- 8 GB RAM minimum (models use ~4.5 GB combined)