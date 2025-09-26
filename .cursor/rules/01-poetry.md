# Poetry Dependency Management Rules

## Project Setup
- **NEVER use pip** - always use Poetry for this project
- This project uses Poetry for all dependency management
- Virtual environment is managed by Poetry automatically

## Common Commands
- Install dependencies: `poetry install`
- Add new dependency: `poetry add package_name`
- Add dev dependency: `poetry add --group dev package_name`
- Update dependencies: `poetry update`
- Run scripts: `poetry run python script.py`
- Run MCP server: `poetry run mcp dev codemagic_mcp/server.py`

## Development Workflow
- Always run tests with Poetry: `poetry run python local_only/run_all_tests.py`
- Install before development: `poetry install`
- Add dependencies only when necessary
- Keep pyproject.toml updated with version constraints

## Testing
- Run all tests: `poetry run python local_only/run_all_tests.py`
- Test with API key: `CODEMAGIC_API_KEY=key poetry run python local_only/run_all_tests.py`
- Individual tests: `poetry run python local_only/test_imports.py`

## MCP Server
- Run server: `poetry run mcp dev codemagic_mcp/server.py`
- Direct run: `poetry run python codemagic_mcp/server.py`
- All MCP commands must use Poetry
