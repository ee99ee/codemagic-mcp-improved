# Build Endpoints Documentation

This document describes the new MCP endpoints added to support comprehensive build monitoring and log analysis in Codemagic.

## Overview

The new endpoints provide detailed access to build information, logs, workflow steps, and artifacts, enabling applications to display comprehensive build status and execution details.

## New Endpoints

### Build Logs & Steps

#### `get_build_logs(build_id: str)`
Get the build logs for a specific build, including step-by-step execution details.

**Parameters:**
- `build_id`: The build identifier

**Returns:** Dictionary containing the build logs with step-by-step details

**Example Usage:**
```python
logs = get_build_logs("build_123")
print(logs['steps'])  # List of build steps with logs
```

#### `get_build_workflow_steps(build_id: str)`
Get the workflow steps and their execution details for a specific build.

**Parameters:**
- `build_id`: The build identifier

**Returns:** Dictionary containing workflow steps with their status, timing, and details

#### `get_build_steps(build_id: str)`
Get the individual steps and their execution details for a specific build.

**Parameters:**
- `build_id`: The build identifier

**Returns:** Dictionary containing build steps with their status, timing, and output

#### `get_build_step_logs(build_id: str, step_id: str)`
Get the logs for a specific step within a build.

**Parameters:**
- `build_id`: The build identifier
- `step_id`: The step identifier

**Returns:** Dictionary containing the step logs and metadata

#### `get_build_timeline(build_id: str)`
Get a timeline of events for a specific build showing the progression through steps.

**Parameters:**
- `build_id`: The build identifier

**Returns:** Dictionary containing the build timeline with timestamps and events

### Enhanced Build Information

#### `get_builds_detailed(app_id=None, workflow_id=None, branch=None, tag=None, limit=None)`
Get a detailed list of builds with enhanced metadata including status, timing, and workflow information.

**Parameters:**
- `app_id`: Optional filter by application identifier
- `workflow_id`: Optional filter by workflow identifier
- `branch`: Optional filter by branch name
- `tag`: Optional filter by tag name
- `limit`: Optional limit on number of builds to return (default: 50)

**Returns:** Dictionary containing detailed builds information with enhanced metadata

#### `get_build_summary(build_id: str)`
Get a comprehensive summary of a build including status, metadata, logs summary, and artifacts.

**Parameters:**
- `build_id`: The build identifier

**Returns:** Dictionary containing comprehensive build summary with all relevant information

**Example Response Structure:**
```json
{
  "build": {
    "_id": "build_123",
    "status": "finished",
    "startedAt": "2024-01-01T10:00:00Z",
    "finishedAt": "2024-01-01T10:30:00Z"
  },
  "logs": {
    "steps": [...],
    "summary": "..."
  },
  "workflow": {
    "steps": [...],
    "status": "completed"
  },
  "artifacts": [...],
  "environment": {...}
}
```

### Build Artifacts & Environment

#### `get_build_artifacts(build_id: str)`
Get all artifacts produced by a specific build.

**Parameters:**
- `build_id`: The build identifier

**Returns:** Dictionary containing the list of artifacts with their details

#### `get_build_environment(build_id: str)`
Get the environment variables and configuration used for a specific build.

**Parameters:**
- `build_id`: The build identifier

**Returns:** Dictionary containing environment variables and build configuration

### Workflow Management

#### `get_workflows(app_id: str)`
Get all workflows for a specific application.

**Parameters:**
- `app_id`: The application identifier

**Returns:** Dictionary containing the list of workflows for the application

#### `get_workflow_details(workflow_id: str)`
Get detailed information about a specific workflow.

**Parameters:**
- `workflow_id`: The workflow identifier

**Returns:** Dictionary containing detailed workflow information

## Usage Examples

### Get Build Status with Logs
```python
# Get comprehensive build information
summary = get_build_summary("build_123")
print(f"Build Status: {summary['build']['status']}")
print(f"Logs Available: {'logs' in summary}")

# Get detailed logs
logs = get_build_logs("build_123")
for step in logs['steps']:
    print(f"Step: {step['name']} - Status: {step['status']}")
```

### Monitor Build Progress
```python
# Get build timeline
timeline = get_build_timeline("build_123")
for event in timeline['events']:
    print(f"{event['timestamp']}: {event['description']}")

# Get individual step details
steps = get_build_steps("build_123")
for step in steps['steps']:
    if step['status'] == 'failed':
        step_logs = get_build_step_logs("build_123", step['id'])
        print(f"Failed step logs: {step_logs['content']}")
```

### List Builds with Enhanced Metadata
```python
# Get detailed builds for an app
detailed_builds = get_builds_detailed(app_id="app_123", limit=10)
for build in detailed_builds['builds']:
    print(f"Build {build['_id']}: {build['status']} - Duration: {build['duration']}")
```

## Error Handling

All endpoints include proper error handling and will return appropriate error messages if:
- The build ID doesn't exist
- The API endpoint is not available
- Authentication fails
- Rate limits are exceeded

## Testing

Run the test suite to verify all endpoints work correctly:

```bash
# Test with API key
CODEMAGIC_API_KEY=your_key poetry run python local_only/test_build_endpoints.py

# Run all tests
poetry run python local_only/run_all_tests.py
```

## Notes

- Some endpoints may not be available in all Codemagic API versions
- The endpoints are designed to gracefully handle missing data
- All endpoints include comprehensive error handling
- The `get_build_summary` endpoint combines multiple API calls for convenience
