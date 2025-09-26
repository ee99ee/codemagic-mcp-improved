# Codemagic MCP Server - Modular Structure

This directory contains the modularized Codemagic MCP server implementation, split into logical modules for better maintainability.

## Module Structure

### `base.py`
Contains common functionality shared across all modules:
- API base URL configuration
- Authentication headers management
- Generic request handling utilities

### `applications.py`
Handles application-related API endpoints:
- `get_all_applications()` - Retrieve all applications
- `get_application(app_id)` - Get specific application details
- `add_application(repository_url, team_id)` - Add new public application
- `add_application_private(...)` - Add new private application with SSH key

### `artifacts.py`
Manages build artifact operations:
- `get_artifact(secure_filename)` - Download artifact content
- `create_public_artifact_url(secure_filename, expires_at)` - Create public download URL

### `builds.py`
Comprehensive build management functionality:
- `start_build(...)` - Start new builds
- `get_builds(...)` - List builds with filtering
- `get_build_status(build_id)` - Get build status
- `cancel_build(build_id)` - Cancel running builds
- `get_build_logs(build_id)` - Retrieve build logs
- `get_build_workflow_steps(build_id)` - Get workflow execution details
- `get_build_artifacts(build_id)` - List build artifacts
- `get_build_environment(build_id)` - Get build environment
- `get_builds_detailed(...)` - Enhanced build listing
- `get_build_summary(build_id)` - Comprehensive build summary

### `workflows.py`
Workflow and step management:
- `get_workflows(app_id)` - List application workflows
- `get_workflow_details(workflow_id)` - Get workflow details
- `get_build_steps(build_id)` - Get build step details
- `get_build_step_logs(build_id, step_id)` - Get step-specific logs
- `get_build_timeline(build_id)` - Get build execution timeline

### `caches.py`
Cache management operations:
- `get_app_caches(app_id)` - List application caches
- `delete_all_app_caches(app_id)` - Delete all caches
- `delete_app_cache(app_id, cache_id)` - Delete specific cache

### `teams.py`
Team management functionality:
- `invite_team_member(team_id, email, role)` - Invite team members
- `delete_team_member(team_id, user_id)` - Remove team members

### `server.py`
Main server module that:
- Creates the FastMCP instance
- Imports and registers all tool modules
- Provides the unified MCP server interface

## Benefits of This Structure

1. **Maintainability**: Each module focuses on a specific API area
2. **Readability**: Smaller, focused files are easier to understand
3. **Testability**: Individual modules can be tested in isolation
4. **Extensibility**: New API endpoints can be added to appropriate modules
5. **Collaboration**: Multiple developers can work on different modules simultaneously

## Adding New Endpoints

To add new API endpoints:

1. Identify the appropriate module based on functionality
2. Add the new tool function to that module
3. The function will be automatically registered when the server starts

## Environment Variables

The server requires the `CODEMAGIC_API_KEY` environment variable to be set for authentication.
