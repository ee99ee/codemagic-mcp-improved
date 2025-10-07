# How to Use Codemagic MCP Server in Other Projects

This guide explains how to use the Codemagic MCP server in other projects on your local machine.

## Prerequisites

1. **Python 3.10+** installed on your system
2. **Poetry** installed (recommended) or pip
3. **Codemagic API Key** (get it from [Codemagic Dashboard](https://codemagic.io/app/))

## Method 1: Using Poetry (Recommended)

### Step 1: Install Dependencies

```bash
# Navigate to the codemagic-mcp-improved directory
cd /Users/cmiller/domains/open-source/codemagic-mcp-improved

# Install dependencies
poetry install
```

### Step 2: Set Up Environment Variables

```bash
# Set your Codemagic API key
export CODEMAGIC_API_KEY="your-api-key-here"

# Or create a .env file
echo "CODEMAGIC_API_KEY=your-api-key-here" > .env
```

### Step 3: Configure MCP Client

#### For Cursor IDE

Create or update your Cursor MCP configuration file:

**Option A: Using Poetry (Recommended)**
```json
{
  "mcpServers": {
    "codemagic": {
      "command": "poetry",
      "args": [
        "run",
        "python",
        "-m",
        "codemagic_mcp.server"
      ],
      "cwd": "/Users/cmiller/domains/open-source/codemagic-mcp-improved",
      "env": {
        "CODEMAGIC_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

**Option B: Using Python directly**
```json
{
  "mcpServers": {
    "codemagic": {
      "command": "python",
      "args": [
        "-m",
        "codemagic_mcp.server"
      ],
      "cwd": "/Users/cmiller/domains/open-source/codemagic-mcp-improved",
      "env": {
        "PYTHONPATH": "/Users/cmiller/domains/open-source/codemagic-mcp-improved",
        "CODEMAGIC_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

#### For Claude Desktop

Add to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "Codemagic MCP Server": {
      "command": "poetry",
      "args": [
        "run",
        "python",
        "-m",
        "codemagic_mcp.server"
      ],
      "cwd": "/Users/cmiller/domains/open-source/codemagic-mcp-improved",
      "env": {
        "CODEMAGIC_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Method 2: Using pip (Alternative)

### Step 1: Install Dependencies

```bash
# Navigate to the codemagic-mcp-improved directory
cd /Users/cmiller/domains/open-source/codemagic-mcp-improved

# Install dependencies
pip install -r requirements.txt
# or
pip install mcp requests
```

### Step 2: Configure MCP Client

```json
{
  "mcpServers": {
    "codemagic": {
      "command": "python",
      "args": [
        "-m",
        "codemagic_mcp.server"
      ],
      "cwd": "/Users/cmiller/domains/open-source/codemagic-mcp-improved",
      "env": {
        "PYTHONPATH": "/Users/cmiller/domains/open-source/codemagic-mcp-improved",
        "CODEMAGIC_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Method 3: Global Installation

### Step 1: Install as a Package

```bash
# Navigate to the codemagic-mcp-improved directory
cd /Users/cmiller/domains/open-source/codemagic-mcp-improved

# Install in development mode
pip install -e .

# Or install globally
pip install .
```

### Step 2: Configure MCP Client

```json
{
  "mcpServers": {
    "codemagic": {
      "command": "python",
      "args": [
        "-m",
        "codemagic_mcp.server"
      ],
      "env": {
        "CODEMAGIC_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

## Testing Your Setup

### Step 1: Test the Server

```bash
# Navigate to the codemagic-mcp-improved directory
cd /Users/cmiller/domains/open-source/codemagic-mcp-improved

# Test with API key
CODEMAGIC_API_KEY=your-api-key poetry run python local_only/test_api_connection.py

# Test all endpoints
CODEMAGIC_API_KEY=your-api-key poetry run python local_only/run_all_tests.py
```

### Step 2: Test MCP Connection

```bash
# Test MCP server directly
poetry run python -m codemagic_mcp.server
```

## Usage Examples

Once configured, you can use the MCP server in your projects:

### In Cursor IDE

```
You: "Show me all my Codemagic applications"
Assistant: *calls get_all_applications() and displays the list*

You: "Start a build for my Flutter app"
Assistant: *calls start_build() with appropriate parameters*

You: "Show me the logs for my latest build"
Assistant: *calls get_build_logs() and displays step-by-step details*

You: "What's the status of my current build?"
Assistant: *calls get_build_summary() and shows comprehensive information*
```

### Available Endpoints

- **Applications**: `get_all_applications`, `get_application`, `add_application`
- **Builds**: `get_builds`, `get_build_status`, `start_build`, `cancel_build`
- **Build Logs**: `get_build_logs`, `get_build_steps`, `get_build_timeline`
- **Artifacts**: `get_artifact`, `get_build_artifacts`
- **Workflows**: `get_workflows`, `get_workflow_details`
- **Caches**: `get_app_caches`, `delete_app_cache`
- **Teams**: `invite_team_member`, `delete_team_member`

## Troubleshooting

### Common Issues

1. **"Module not found" error**
   - Make sure `PYTHONPATH` is set correctly
   - Use absolute paths in your MCP configuration

2. **"API key not found" error**
   - Set the `CODEMAGIC_API_KEY` environment variable
   - Check that the API key is valid

3. **"Permission denied" error**
   - Make sure the `cwd` path is correct and accessible
   - Check file permissions

### Debug Mode

```bash
# Run with debug output
CODEMAGIC_API_KEY=your-key poetry run python -m codemagic_mcp.server --debug

# Test specific endpoint
CODEMAGIC_API_KEY=your-key poetry run python -c "
from codemagic_mcp.server import get_all_applications
print(get_all_applications())
"
```

## Configuration Files

The project includes several configuration files:

- `.cursor/mcp.json` - Cursor IDE configuration
- `.cursor/mcp-alternative.json` - Alternative configuration
- `pyproject.toml` - Poetry project configuration
- `.env.example` - Environment variables template

## Next Steps

1. **Get your Codemagic API key** from the [Codemagic Dashboard](https://codemagic.io/app/)
2. **Choose your preferred method** (Poetry recommended)
3. **Configure your MCP client** with the appropriate settings
4. **Test the connection** using the provided test scripts
5. **Start using the endpoints** in your projects!

## Support

- **Documentation**: Check `BUILD_ENDPOINTS.md` for detailed endpoint documentation
- **Issues**: Report issues on the [GitHub repository](https://github.com/ee99ee/codemagic-mcp-improved)
- **Contributing**: See `CONTRIBUTING.md` for contribution guidelines
