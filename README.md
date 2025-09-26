<div align="center">

# Codemagic MCP Server

</div>

---

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey.svg)
![Build Status](https://img.shields.io/badge/build-passing-green.svg)
![](https://badge.mcpx.dev?type=server 'MCP Server')

</div>

---

A lightweight, community-maintained [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) server that provides seamless access to `Codemagic CI/CD` APIs. Built for agents, AI-native workflows, and for use of MCP-compatible clients.

---

## 🌐 How can you use this

**You:** What applications do I have on Codemagic?  
**Assistant:** *calls `get_all_applications()` and displays the list.*

**You:** Start a new build for my Flutter app  
**Assistant:** *calls `start_build()` with appropriate parameters*

**You:** Can you get the artifacts from my last build?  
**Assistant:** *calls `get_builds()` to find the latest build and then `get_artifact()` to download the files*

**You:** Show me the cache usage for my app  
**Assistant:** *calls `get_app_caches()` and displays storage information*

**You:** Show me the logs for my latest build with step-by-step details  
**Assistant:** *calls `get_build_logs()` and `get_build_steps()` to show detailed execution logs*

**You:** What's the status and timeline of my current build?  
**Assistant:** *calls `get_build_summary()` and `get_build_timeline()` to show comprehensive build information*

**You:** Show me all the workflows available for my app  
**Assistant:** *calls `get_workflows()` to list all available workflows and their configurations*

---

## 🌐 Getting started

### 1. Clone this repository

```bash
git clone https://github.com/ee99ee/codemagic-mcp-improved.git
cd codemagic-mcp-improved
```

### 2. Set up your API key

Follow the [official documentation](https://docs.codemagic.io/rest-api/codemagic-rest-api/).

### 3. Install the MCP server in your client

For example, for [Claude Desktop](https://claude.ai/download): 

```
{
  "mcpServers": {
    "Codemagic MCP Server": {
      "command": "poetry",
      "args": [
        "run",
        "mcp",
        "run",
        "<global_path_to_the_cloned_repo>/codemagic_mcp/server.py"
      ],
      "env": {
        "CODEMAGIC_API_KEY": "your-api-key-here"
      }
    },
}
```

---

## 📈 What this server can do

Interact with Codemagic CI/CD using natural language.

| API Category | Tools |
|:---|:---|
| **Applications API** | `get_all_applications`, `get_application`, `add_application`, `add_application_private` |
| **Artifacts API** | `get_artifact`, `create_public_artifact_url` |
| **Builds API** | `start_build`, `get_builds`, `get_build_status`, `cancel_build`, `get_builds_detailed`, `get_build_summary` |
| **Build Logs & Steps** | `get_build_logs`, `get_build_workflow_steps`, `get_build_steps`, `get_build_step_logs`, `get_build_timeline` |
| **Build Artifacts & Environment** | `get_build_artifacts`, `get_build_environment` |
| **Workflows API** | `get_workflows`, `get_workflow_details` |
| **Caches API** | `get_app_caches`, `delete_all_app_caches`, `delete_app_cache` |
| **Teams API** | `invite_team_member`, `delete_team_member` |

---

## 🛠️ Development

### Installation

```bash
# Install dependencies
poetry install
```

### Testing

Run the test suite to verify everything works:

```bash
# Run all tests (basic functionality)
poetry run python local_only/run_all_tests.py

# Run with API key for full testing
CODEMAGIC_API_KEY=your_key poetry run python local_only/run_all_tests.py
```

### Running the Server

```bash
# Run the server in development mode
poetry run mcp dev codemagic_mcp/server.py

# Or run directly
poetry run python codemagic_mcp/server.py
```

### Test Scripts

The `local_only/` directory contains test scripts (excluded from git):
- `test_imports.py` - Verify all imports work
- `test_mcp_server.py` - Test server functionality  
- `test_api_connection.py` - Test with real API (requires API key)
- `run_all_tests.py` - Run all tests in sequence

---

## 📚 References

- [Codemagic REST API Documentation](https://docs.codemagic.io/rest-api/overview/)
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)

---

## 📜 License

[MIT License](LICENSE) © 2025 Stefano Amorelli

This is a fork of the original [codemagic-mcp](https://github.com/stefanoamorelli/codemagic-mcp) repository with improvements and updates.
