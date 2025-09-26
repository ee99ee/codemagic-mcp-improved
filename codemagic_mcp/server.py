"""
Main Codemagic MCP server module.
"""
from mcp.server.fastmcp import FastMCP

# Import all module registration functions
from .applications import register_applications_tools
from .artifacts import register_artifacts_tools
from .builds import register_builds_tools
from .workflows import register_workflows_tools
from .caches import register_caches_tools
from .teams import register_teams_tools

# Create the MCP server instance
mcp = FastMCP("Codemagic MCP", dependencies=["requests"])

# Register all tools from each module
register_applications_tools(mcp)
register_artifacts_tools(mcp)
register_builds_tools(mcp)
register_workflows_tools(mcp)
register_caches_tools(mcp)
register_teams_tools(mcp)
