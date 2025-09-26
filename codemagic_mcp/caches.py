"""
Caches API module for Codemagic MCP server.
"""
from mcp.server.fastmcp import FastMCP
from typing import Dict, Any, List
from .base import make_request


def register_caches_tools(mcp: FastMCP) -> None:
    """Register all cache-related tools with the MCP server."""
    
    @mcp.tool()
    def get_app_caches(app_id: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Retrieve a list of caches for an application.
        
        Args:
            app_id: The application identifier
            
        Returns:
            Dictionary containing the list of caches for the application
        """
        response = make_request("GET", f"/apps/{app_id}/caches")
        return response.json()

    @mcp.tool()
    def delete_all_app_caches(app_id: str) -> Dict[str, Any]:
        """
        Delete all stored caches for an application.
        
        Args:
            app_id: The application identifier
            
        Returns:
            Dictionary with the list of cache IDs that will be deleted and a message
        """
        response = make_request("DELETE", f"/apps/{app_id}/caches")
        # API returns 202 Accepted for successful cache deletion
        if response.status_code == 202:
            return response.json()
        return response.json()

    @mcp.tool()
    def delete_app_cache(app_id: str, cache_id: str) -> Dict[str, Any]:
        """
        Delete a specific cache from an application.
        
        Args:
            app_id: The application identifier
            cache_id: The cache identifier to delete
            
        Returns:
            Dictionary with the deleted cache ID and a message
        """
        response = make_request("DELETE", f"/apps/{app_id}/caches/{cache_id}")
        # API returns 202 Accepted for successful cache deletion
        if response.status_code == 202:
            return response.json()
        return response.json()
