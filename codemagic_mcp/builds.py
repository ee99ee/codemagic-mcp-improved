"""
Builds API module for Codemagic MCP server.
"""
from mcp.server.fastmcp import FastMCP
from typing import Optional, Dict, Any, List
from .base import make_request


def register_builds_tools(mcp: FastMCP) -> None:
    """Register all build-related tools with the MCP server."""
    
    @mcp.tool()
    def start_build(
        app_id: str,
        workflow_id: str,
        branch: Optional[str] = None,
        tag: Optional[str] = None,
        environment: Optional[Dict[str, Any]] = None,
        labels: Optional[List[str]] = None,
        instance_type: Optional[str] = None
    ) -> Dict[str, str]:
        """
        Start a new build on Codemagic.
        
        Args:
            app_id: The application identifier
            workflow_id: The workflow identifier
            branch: The branch name (either branch or tag is required)
            tag: The tag name (either branch or tag is required)
            environment: Dictionary with environment variables, variable groups, and software versions
            labels: List of labels to include for the build
            instance_type: Type of instance to use for the build (e.g. 'mac_mini_m2')
            
        Returns:
            Dictionary with the build ID
        """
        if not branch and not tag:
            raise ValueError("Either branch or tag must be provided")
        
        data = {
            "appId": app_id,
            "workflowId": workflow_id
        }
        
        if branch:
            data["branch"] = branch
        if tag:
            data["tag"] = tag
        if environment:
            data["environment"] = environment
        if labels:
            data["labels"] = labels
        if instance_type:
            data["instanceType"] = instance_type
        
        response = make_request("POST", "/builds", json=data)
        return response.json()

    @mcp.tool()
    def get_builds(
        app_id: Optional[str] = None,
        workflow_id: Optional[str] = None,
        branch: Optional[str] = None,
        tag: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get a list of builds from Codemagic build history.
        
        Args:
            app_id: Optional filter by application identifier
            workflow_id: Optional filter by workflow identifier
            branch: Optional filter by branch name
            tag: Optional filter by tag name
            
        Returns:
            Dictionary containing applications and builds information
        """
        params = {}
        if app_id:
            params["appId"] = app_id
        if workflow_id:
            params["workflowId"] = workflow_id
        if branch:
            params["branch"] = branch
        if tag:
            params["tag"] = tag
        
        response = make_request("GET", "/builds", params=params)
        return response.json()

    @mcp.tool()
    def get_build_status(build_id: str) -> Dict[str, Any]:
        """
        Get the status of a build on Codemagic.
        
        Args:
            build_id: The build identifier
            
        Returns:
            Dictionary containing the application and build information
        """
        response = make_request("GET", f"/builds/{build_id}")
        return response.json()

    @mcp.tool()
    def cancel_build(build_id: str) -> Dict[str, Any]:
        """
        Cancel a running build on Codemagic.
        
        Args:
            build_id: The build identifier
            
        Returns:
            Response from the API (empty if successful)
        """
        response = make_request("POST", f"/builds/{build_id}/cancel")
        if response.status_code == 208:  # Already Reported (build already finished)
            return {"message": "Build has already finished"}
        return response.json() if response.content else {}

    @mcp.tool()
    def get_build_logs(build_id: str) -> Dict[str, Any]:
        """
        Get the build logs for a specific build, including step-by-step execution details.
        
        Args:
            build_id: The build identifier
            
        Returns:
            Dictionary containing the build logs with step-by-step details
        """
        response = make_request("GET", f"/builds/{build_id}/logs")
        return response.json()

    @mcp.tool()
    def get_build_workflow_steps(build_id: str) -> Dict[str, Any]:
        """
        Get the workflow steps and their execution details for a specific build.
        
        Args:
            build_id: The build identifier
            
        Returns:
            Dictionary containing workflow steps with their status, timing, and details
        """
        response = make_request("GET", f"/builds/{build_id}/workflow")
        return response.json()

    @mcp.tool()
    def get_build_artifacts(build_id: str) -> Dict[str, Any]:
        """
        Get all artifacts produced by a specific build.
        
        Args:
            build_id: The build identifier
            
        Returns:
            Dictionary containing the list of artifacts with their details
        """
        response = make_request("GET", f"/builds/{build_id}/artifacts")
        return response.json()

    @mcp.tool()
    def get_build_environment(build_id: str) -> Dict[str, Any]:
        """
        Get the environment variables and configuration used for a specific build.
        
        Args:
            build_id: The build identifier
            
        Returns:
            Dictionary containing environment variables and build configuration
        """
        response = make_request("GET", f"/builds/{build_id}/environment")
        return response.json()

    @mcp.tool()
    def get_builds_detailed(
        app_id: Optional[str] = None,
        workflow_id: Optional[str] = None,
        branch: Optional[str] = None,
        tag: Optional[str] = None,
        limit: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Get a detailed list of builds with enhanced metadata including status, timing, and workflow information.
        
        Args:
            app_id: Optional filter by application identifier
            workflow_id: Optional filter by workflow identifier
            branch: Optional filter by branch name
            tag: Optional filter by tag name
            limit: Optional limit on number of builds to return (default: 50)
            
        Returns:
            Dictionary containing detailed builds information with enhanced metadata
        """
        params = {}
        if app_id:
            params["appId"] = app_id
        if workflow_id:
            params["workflowId"] = workflow_id
        if branch:
            params["branch"] = branch
        if tag:
            params["tag"] = tag
        if limit:
            params["limit"] = limit
        
        response = make_request("GET", "/builds/detailed", params=params)
        return response.json()

    @mcp.tool()
    def get_build_summary(build_id: str) -> Dict[str, Any]:
        """
        Get a comprehensive summary of a build including status, metadata, logs summary, and artifacts.
        
        Args:
            build_id: The build identifier
            
        Returns:
            Dictionary containing comprehensive build summary with all relevant information
        """
        # Get basic build info
        build_info = get_build_status(build_id)
        
        # Get additional details
        try:
            logs = get_build_logs(build_id)
        except:
            logs = {"error": "Logs not available"}
        
        try:
            workflow = get_build_workflow_steps(build_id)
        except:
            workflow = {"error": "Workflow steps not available"}
        
        try:
            artifacts = get_build_artifacts(build_id)
        except:
            artifacts = {"error": "Artifacts not available"}
        
        try:
            environment = get_build_environment(build_id)
        except:
            environment = {"error": "Environment not available"}
        
        return {
            "build": build_info,
            "logs": logs,
            "workflow": workflow,
            "artifacts": artifacts,
            "environment": environment
        }
