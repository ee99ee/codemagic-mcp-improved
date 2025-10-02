"""
Base module for Codemagic MCP server with common functionality.
"""
import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv


# Global variables
BASE_URL = "https://api.codemagic.io"

# Load environment variables from .env file
load_dotenv()


def get_headers() -> Dict[str, str]:
    """Get headers for Codemagic API requests with API token from environment"""
    api_token = os.environ.get("CODEMAGIC_API_KEY")
    if not api_token:
        raise ValueError("CODEMAGIC_API_KEY environment variable is required")
    
    return {
        "Content-Type": "application/json",
        "x-auth-token": api_token
    }


def make_request(method: str, endpoint: str, **kwargs) -> requests.Response:
    """
    Make a request to the Codemagic API with proper error handling.
    
    Args:
        method: HTTP method (GET, POST, DELETE, etc.)
        endpoint: API endpoint (without base URL)
        **kwargs: Additional arguments for requests
        
    Returns:
        Response object
    """
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    headers = get_headers()
    
    # Merge headers if provided
    if 'headers' in kwargs:
        headers.update(kwargs.pop('headers'))
    
    response = requests.request(method, url, headers=headers, **kwargs)
    response.raise_for_status()
    return response
