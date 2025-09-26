# Security Rules

## API Keys & Secrets
- Never commit API keys or sensitive data
- Use environment variables for configuration
- Include security warnings in documentation
- Provide clear instructions for key management

## Data Handling
- Don't log sensitive API responses
- Sanitize user input before API calls
- Implement proper error boundaries
- Respect rate limits and API quotas

## Testing
- Test with real API keys in development only
- Use Poetry for all testing: `poetry run python local_only/run_all_tests.py`
- Revoke test API keys after development
- Never commit test API keys or sensitive data
- Set API key: `CODEMAGIC_API_KEY=key poetry run python local_only/test_api_connection.py`
