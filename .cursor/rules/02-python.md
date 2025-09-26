# Python Development Rules

## Code Style
- Use Python 3.10+ features and type hints
- Follow PEP 8 style guidelines
- Use f-strings for string formatting
- Prefer explicit imports over wildcard imports
- Add docstrings to all public functions and classes

## Dependencies
- **ALWAYS use Poetry** for dependency management (never pip)
- Add dependencies with: `poetry add package_name`
- Add dev dependencies with: `poetry add --group dev package_name`
- Pin dependency versions in pyproject.toml
- Keep dependencies up to date with: `poetry update`
- Install dependencies with: `poetry install`
- Run scripts with: `poetry run python script.py`

## Testing
- All test scripts go in `local_only/` directory
- Run tests with: `poetry run python local_only/run_all_tests.py`
- Use proper error handling and exit codes
- Include descriptive output with emojis for clarity
- Make scripts executable and self-contained
- Test with API key: `CODEMAGIC_API_KEY=key poetry run python local_only/run_all_tests.py`
