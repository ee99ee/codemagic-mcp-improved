"""
Artifacts API module for Codemagic MCP server.
"""
from mcp.server.fastmcp import FastMCP
from typing import Dict, Any
from .base import make_request


def register_artifacts_tools(mcp: FastMCP) -> None:
    """Register all artifact-related tools with the MCP server."""
    
    @mcp.tool()
    def get_artifact(secure_filename: str) -> bytes:
        """
        Get authenticated download URL for a build artifact.
        
        Args:
            secure_filename: The secure filename of the artifact (from Builds API or Codemagic UI)
                             Format: uuid1/uuid2/filename.ext
        
        Returns:
            The artifact file content as bytes
        """
        response = make_request("GET", f"/artifacts/{secure_filename}")
        return response.content

    @mcp.tool()
    def create_public_artifact_url(secure_filename: str, expires_at: int) -> Dict[str, Any]:
        """
        Create a public download URL for a build artifact.
        
        Args:
            secure_filename: The secure filename of the artifact (from Builds API or Codemagic UI)
                             Format: uuid1/uuid2/filename.ext
            expires_at: URL expiration UNIX timestamp in seconds
            
        Returns:
            Dictionary containing the public artifact URL and expiration timestamp
        """
        data = {"expiresAt": expires_at}
        
        response = make_request(
            "POST",
            f"/artifacts/{secure_filename}/public-url", 
            json=data
        )
        return response.json()
