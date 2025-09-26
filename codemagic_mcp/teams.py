"""
Teams API module for Codemagic MCP server.
"""
from mcp.server.fastmcp import FastMCP
from typing import Dict, Any
from .base import make_request


def register_teams_tools(mcp: FastMCP) -> None:
    """Register all team-related tools with the MCP server."""
    
    @mcp.tool()
    def invite_team_member(team_id: str, email: str, role: str) -> Dict[str, Any]:
        """
        Invite a new team member to your team.
        
        Args:
            team_id: The team identifier
            email: User email to invite
            role: User role, can be 'owner' (Admin) or 'developer' (Member)
            
        Returns:
            Full team object
        """
        if role not in ["owner", "developer"]:
            raise ValueError("Role must be either 'owner' or 'developer'")
        
        data = {
            "email": email,
            "role": role
        }
        
        response = make_request("POST", f"/team/{team_id}/invitation", json=data)
        return response.json()

    @mcp.tool()
    def delete_team_member(team_id: str, user_id: str) -> Dict[str, Any]:
        """
        Remove a team member from the team.
        
        Args:
            team_id: The team identifier
            user_id: The user identifier to remove
            
        Returns:
            Response from the API (empty if successful)
        """
        response = make_request("DELETE", f"/team/{team_id}/collaborator/{user_id}")
        return response.json() if response.content else {}
