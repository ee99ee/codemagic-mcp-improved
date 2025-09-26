"""
Applications API module for Codemagic MCP server.
"""
from mcp.server.fastmcp import FastMCP
from typing import Optional, Dict, Any, List
from .base import make_request


def register_applications_tools(mcp: FastMCP) -> None:
    """Register all application-related tools with the MCP server."""
    
    @mcp.tool()
    def get_all_applications() -> Dict[str, List[Dict[str, Any]]]:
        """
        Retrieve all applications from Codemagic.
            
        Returns:
            Dictionary containing the applications
        """
        response = make_request("GET", "/apps")
        return response.json()

    @mcp.tool()
    def get_application(app_id: str) -> Dict[str, Dict[str, Any]]:
        """
        Retrieve a specific application from Codemagic by ID.
        
        Args:
            app_id: Application ID
            
        Returns:
            Dictionary containing the application details
        """
        response = make_request("GET", f"/apps/{app_id}")
        return response.json()

    @mcp.tool()
    def add_application(repository_url: str, team_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Add a new application to Codemagic.
        
        Args:
            repository_url: SSH or HTTPS URL for cloning the repository
            team_id: Optional team ID to add the app directly to a team (must be admin)
            
        Returns:
            Dictionary containing the created application details
        """
        data = {"repositoryUrl": repository_url}
        if team_id:
            data["teamId"] = team_id
            
        response = make_request("POST", "/apps", json=data)
        return response.json()

    @mcp.tool()
    def add_application_private(
        repository_url: str,
        ssh_key_data: str,
        ssh_key_passphrase: Optional[str] = None,
        project_type: Optional[str] = None,
        team_id: Optional[str] = None
    ) -> Dict[str, Dict[str, Any]]:
        """
        Add a new application from a private repository to Codemagic.
        
        Args:
            repository_url: SSH or HTTPS URL for cloning the repository
            ssh_key_data: base64-encoded private key file
            ssh_key_passphrase: SSH key passphrase or None if the SSH key is without a passphrase
            project_type: Set to "flutter-app" when adding Flutter application
            team_id: Optional team ID to add the app directly to a team (must be admin)
            
        Returns:
            Dictionary containing the created application details
        """
        data = {
            "repositoryUrl": repository_url,
            "sshKey": {
                "data": ssh_key_data,
                "passphrase": ssh_key_passphrase
            }
        }
        
        if project_type:
            data["projectType"] = project_type
            
        if team_id:
            data["teamId"] = team_id
            
        response = make_request("POST", "/apps/new", json=data)
        return response.json()
