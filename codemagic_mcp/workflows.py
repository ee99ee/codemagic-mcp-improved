"""
Workflows API module for Codemagic MCP server.
"""
from mcp.server.fastmcp import FastMCP
from typing import Dict, Any
from .base import make_request


def register_workflows_tools(mcp: FastMCP) -> None:
    """Register all workflow-related tools with the MCP server."""
    
    @mcp.tool()
    def get_workflows(app_id: str) -> Dict[str, Any]:
        """
        Get all workflows for a specific application.
        
        Args:
            app_id: The application identifier
            
        Returns:
            Dictionary containing the list of workflows for the application
        """
        response = make_request("GET", f"/apps/{app_id}/workflows")
        return response.json()

    @mcp.tool()
    def get_workflow_details(workflow_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific workflow.
        
        Args:
            workflow_id: The workflow identifier
            
        Returns:
            Dictionary containing detailed workflow information
        """
        response = make_request("GET", f"/workflows/{workflow_id}")
        return response.json()

    @mcp.tool()
    def get_build_steps(build_id: str) -> Dict[str, Any]:
        """
        Get the individual steps and their execution details for a specific build.
        
        Args:
            build_id: The build identifier
            
        Returns:
            Dictionary containing build steps with their status, timing, and output
        """
        response = make_request("GET", f"/builds/{build_id}/steps")
        return response.json()

    @mcp.tool()
    def get_build_step_logs(build_id: str, step_id: str) -> Dict[str, Any]:
        """
        Get the logs for a specific step within a build.
        
        Args:
            build_id: The build identifier
            step_id: The step identifier
            
        Returns:
            Dictionary containing the step logs and metadata
        """
        response = make_request("GET", f"/builds/{build_id}/steps/{step_id}/logs")
        return response.json()

    @mcp.tool()
    def get_build_timeline(build_id: str) -> Dict[str, Any]:
        """
        Get a timeline of events for a specific build showing the progression through steps.
        
        Args:
            build_id: The build identifier
            
        Returns:
            Dictionary containing the build timeline with timestamps and events
        """
        response = make_request("GET", f"/builds/{build_id}/timeline")
        return response.json()
