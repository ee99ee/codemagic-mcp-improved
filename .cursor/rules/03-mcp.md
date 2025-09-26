# MCP Server Development Rules

## Tool Development
- Each tool should have a single, clear purpose
- Include parameter validation
- Provide helpful error messages
- Document return value structure
- All MCP tools should have clear, descriptive names
- Include comprehensive docstrings with parameter descriptions

## API Integration
- Always use environment variables for sensitive data (API keys)
- Implement proper error handling for network requests
- Include timeout handling for API calls
- Log API responses for debugging (without sensitive data)
- Handle API errors gracefully with meaningful error messages
- Use proper HTTP status code handling
- Validate input parameters before making API calls

## Server Configuration
- Use FastMCP for server implementation
- Configure proper CORS if needed
- Implement graceful shutdown
- Add health check endpoints
