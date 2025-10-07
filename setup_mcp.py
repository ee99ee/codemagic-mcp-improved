#!/usr/bin/env python3
"""
Setup script to help configure the Codemagic MCP server for use in other projects.
"""

import os
import json
import sys
from pathlib import Path

def get_project_root():
    """Get the absolute path to the project root."""
    return Path(__file__).parent.absolute()

def create_cursor_config(api_key=None):
    """Create Cursor IDE MCP configuration."""
    project_root = get_project_root()
    
    config = {
        "mcpServers": {
            "codemagic": {
                "command": "poetry",
                "args": [
                    "run",
                    "python",
                    "-m",
                    "codemagic_mcp.server"
                ],
                "cwd": str(project_root)
            }
        }
    }
    
    if api_key:
        config["mcpServers"]["codemagic"]["env"] = {
            "CODEMAGIC_API_KEY": api_key
        }
    
    return config

def create_claude_config(api_key=None):
    """Create Claude Desktop MCP configuration."""
    project_root = get_project_root()
    
    config = {
        "mcpServers": {
            "Codemagic MCP Server": {
                "command": "poetry",
                "args": [
                    "run",
                    "python",
                    "-m",
                    "codemagic_mcp.server"
                ],
                "cwd": str(project_root)
            }
        }
    }
    
    if api_key:
        config["mcpServers"]["Codemagic MCP Server"]["env"] = {
            "CODEMAGIC_API_KEY": api_key
        }
    
    return config

def create_python_config(api_key=None):
    """Create Python-based MCP configuration."""
    project_root = get_project_root()
    
    config = {
        "mcpServers": {
            "codemagic": {
                "command": "python",
                "args": [
                    "-m",
                    "codemagic_mcp.server"
                ],
                "cwd": str(project_root),
                "env": {
                    "PYTHONPATH": str(project_root)
                }
            }
        }
    }
    
    if api_key:
        config["mcpServers"]["codemagic"]["env"]["CODEMAGIC_API_KEY"] = api_key
    
    return config

def main():
    """Main setup function."""
    print("🚀 Codemagic MCP Server Setup")
    print("=" * 40)
    
    # Get API key
    api_key = os.environ.get('CODEMAGIC_API_KEY')
    if not api_key:
        api_key = input("Enter your Codemagic API key (or press Enter to skip): ").strip()
        if not api_key:
            print("⚠️  No API key provided. You'll need to set CODEMAGIC_API_KEY environment variable.")
    
    # Get configuration type
    print("\nSelect configuration type:")
    print("1. Cursor IDE (recommended)")
    print("2. Claude Desktop")
    print("3. Python-based")
    print("4. All configurations")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    project_root = get_project_root()
    configs = {}
    
    if choice in ['1', '4']:
        configs['cursor_config.json'] = create_cursor_config(api_key)
    
    if choice in ['2', '4']:
        configs['claude_config.json'] = create_claude_config(api_key)
    
    if choice in ['3', '4']:
        configs['python_config.json'] = create_python_config(api_key)
    
    # Write configurations
    for filename, config in configs.items():
        filepath = project_root / filename
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"✅ Created {filename}")
    
    # Create .env file if API key provided
    if api_key:
        env_file = project_root / '.env'
        with open(env_file, 'w') as f:
            f.write(f"CODEMAGIC_API_KEY={api_key}\n")
        print("✅ Created .env file")
    
    print(f"\n📁 Configuration files created in: {project_root}")
    print("\n📋 Next steps:")
    print("1. Copy the appropriate config file to your MCP client")
    print("2. For Cursor: Copy cursor_config.json to your Cursor MCP settings")
    print("3. For Claude: Copy claude_config.json to your Claude Desktop settings")
    print("4. Test the connection using: poetry run python local_only/test_api_connection.py")
    
    if not api_key:
        print("\n⚠️  Remember to set your CODEMAGIC_API_KEY environment variable!")

if __name__ == "__main__":
    main()
