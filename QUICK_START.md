# Quick Start Guide

## 🚀 Get Started in 3 Steps

### 1. Set Up Environment
```bash
# Navigate to the project
cd /Users/cmiller/domains/open-source/codemagic-mcp-improved

# Install dependencies
poetry install

# Set your API key
export CODEMAGIC_API_KEY="your-api-key-here"
```

### 2. Generate Configuration
```bash
# Run the setup script
poetry run python setup_mcp.py

# Or manually copy one of these configs:
```

### 3. Configure Your MCP Client

#### For Cursor IDE:
```json
{
  "mcpServers": {
    "codemagic": {
      "command": "poetry",
      "args": ["run", "python", "-m", "codemagic_mcp.server"],
      "cwd": "/Users/cmiller/domains/open-source/codemagic-mcp-improved",
      "env": {"CODEMAGIC_API_KEY": "your-api-key-here"}
    }
  }
}
```

#### For Claude Desktop:
```json
{
  "mcpServers": {
    "Codemagic MCP Server": {
      "command": "poetry",
      "args": ["run", "python", "-m", "codemagic_mcp.server"],
      "cwd": "/Users/cmiller/domains/open-source/codemagic-mcp-improved",
      "env": {"CODEMAGIC_API_KEY": "your-api-key-here"}
    }
  }
}
```

## 🧪 Test Your Setup
```bash
# Test API connection
CODEMAGIC_API_KEY=your-key poetry run python local_only/test_api_connection.py

# Test all endpoints
CODEMAGIC_API_KEY=your-key poetry run python local_only/run_all_tests.py
```

## 💡 Usage Examples
```
You: "Show me my Codemagic applications"
You: "Start a build for my Flutter app"
You: "Show me the logs for my latest build"
You: "What's the status of my current build?"
```

## 📚 Available Endpoints
- **Applications**: `get_all_applications`, `get_application`, `add_application`
- **Builds**: `get_builds`, `get_build_status`, `start_build`, `cancel_build`
- **Logs**: `get_build_logs`, `get_build_steps`, `get_build_timeline`
- **Artifacts**: `get_artifact`, `get_build_artifacts`
- **Workflows**: `get_workflows`, `get_workflow_details`

## 🔧 Troubleshooting
- **Module not found**: Check `PYTHONPATH` and `cwd` paths
- **API key error**: Set `CODEMAGIC_API_KEY` environment variable
- **Permission denied**: Check file permissions and paths

## 📖 Full Documentation
- See `USAGE_GUIDE.md` for detailed instructions
- See `BUILD_ENDPOINTS.md` for endpoint documentation
- See `README.md` for project overview
