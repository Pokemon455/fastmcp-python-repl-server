# Deploy - Python MCP Server

A Python REPL MCP (Model Context Protocol) server built with FastMCP.

## What it does
Runs Python code remotely via MCP protocol — connect it to any AI assistant that supports MCP.

## Tools Available
| Tool | Description |
|------|-------------|
| `run_python` | Execute any Python code and get the output |

## Setup

```bash
git clone https://github.com/Pokemon455/Deploy-.git
cd Deploy-
pip install -r requirements.txt
```

## Run Locally

```bash
python main.py
```

Server starts at: `http://localhost:10000/mcp`

## Deploy on Render
1. Connect this repo to [Render](https://render.com)
2. Set start command: `python main.py`
3. Done!

## Connect to Claude
Add this MCP server URL in Claude.ai connectors:
```
https://your-render-url.onrender.com/mcp
```

## Requirements
- fastmcp
- langchain-experimental
- uvicorn

## Author
- GitHub: [@Pokemon455](https://github.com/Pokemon455)
