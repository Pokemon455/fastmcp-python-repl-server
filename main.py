"""
FastMCP Python REPL Server
==========================
A lightweight MCP (Model Context Protocol) server that exposes a Python REPL
as an AI-callable tool. Any MCP-compatible AI (e.g. Claude) can invoke the
`run_python` tool to execute arbitrary Python code and receive the output.

How it works:
    1. FastMCP creates an MCP server named "Prod MCP"
    2. LangChain's PythonREPLTool handles actual code execution
    3. The server listens over Streamable-HTTP transport
    4. Claude (or any MCP client) sends code → server executes → returns output

Deployment:
    - Render / Railway: PORT env variable is auto-set by the platform
    - Local: defaults to port 10000
    - MCP endpoint: http://<host>:<port>/mcp

Usage (Claude.ai):
    Add this URL in Claude.ai → Settings → Connectors:
    https://your-render-url.onrender.com/mcp
"""

# server.py
import os
from fastmcp import FastMCP                                    # MCP server framework
from langchain_experimental.tools.python.tool import PythonREPLTool  # Python code executor

# ─── MCP Server Initialization ───────────────────────────────────────────────
# Creates an MCP server instance with the given name.
# This name appears in the AI's tool list when connected.
mcp = FastMCP("Prod MCP")

# ─── Python REPL Tool Setup ──────────────────────────────────────────────────
# PythonREPLTool from LangChain runs Python code in a local REPL environment.
# It captures stdout/stderr and returns the result as a string.
python_tool = PythonREPLTool()

# ─── MCP Tool Definition ─────────────────────────────────────────────────────
@mcp.tool()
def run_python(code: str) -> str:
    """
    Execute Python code and return the output.

    This tool allows any connected AI assistant to run Python code
    on this server and get back the result instantly.

    Args:
        code (str): Valid Python code to execute.

    Returns:
        str: Output of the executed code (stdout/stderr).

    Example:
        Input:  "print(sum([1, 2, 3]))"
        Output: "6"
    """
    return str(python_tool.invoke(code))

# ─── Server Entry Point ───────────────────────────────────────────────────────
if __name__ == "__main__":
    # Read PORT from environment variable (set automatically by Render/Railway).
    # Falls back to 10000 for local development.
    port = int(os.getenv("PORT", 10000))

    # Start the MCP server with Streamable-HTTP transport.
    # - host="0.0.0.0"  → accept connections from any IP (required for cloud)
    # - path="/mcp"      → MCP endpoint URL path
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port,
        path="/mcp"
    )
