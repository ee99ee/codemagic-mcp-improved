# Contributing to Codemagic MCP Server

Thank you for your interest in contributing to the Codemagic MCP Server! This document provides guidelines for contributing to this open-source project.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Poetry for dependency management
- Git for version control

### Development Setup

1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/codemagic-mcp-improved.git
   cd codemagic-mcp-improved
   ```

3. **Install dependencies**:
   ```bash
   poetry install
   ```

4. **Run tests** to verify setup:
   ```bash
   poetry run python local_only/run_all_tests.py
   ```

## 🧪 Testing

### Running Tests

```bash
# Basic tests (no API key needed)
poetry run python local_only/run_all_tests.py

# Full tests (with API key)
CODEMAGIC_API_KEY=your_key poetry run python local_only/run_all_tests.py
```

### Test Scripts

- `local_only/test_imports.py` - Verify all imports work
- `local_only/test_mcp_server.py` - Test server functionality
- `local_only/test_api_connection.py` - Test with real API
- `local_only/run_all_tests.py` - Run all tests

## 📝 Code Style

### Python Standards

- Follow PEP 8 style guidelines
- Use type hints for all function parameters and return values
- Add docstrings to all public functions and classes
- Use f-strings for string formatting
- Prefer explicit imports over wildcard imports

### MCP Development

- All MCP tools should have clear, descriptive names
- Include comprehensive docstrings with parameter descriptions
- Handle API errors gracefully with meaningful error messages
- Validate input parameters before making API calls

### Code Formatting

```bash
# Format code with black
poetry run black codemagic_mcp/

# Check code style with flake8
poetry run flake8 codemagic_mcp/

# Type checking with mypy
poetry run mypy codemagic_mcp/
```

## 🔧 Development Workflow

### Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines

3. **Run tests** to ensure nothing is broken:
   ```bash
   poetry run python local_only/run_all_tests.py
   ```

4. **Commit your changes** with descriptive messages:
   ```bash
   git add .
   git commit -m "feat: add new MCP tool for X functionality"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** on GitHub

### Commit Message Format

Use conventional commit messages:

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `test:` - Test additions or changes
- `refactor:` - Code refactoring
- `chore:` - Maintenance tasks

Examples:
- `feat: add new build status tool`
- `fix: handle API timeout errors gracefully`
- `docs: update installation instructions`

## 🔒 Security

### API Keys and Secrets

- **Never commit API keys** or sensitive data
- Use environment variables for configuration
- Test with your own API keys in development
- Revoke test API keys after development

### Data Handling

- Don't log sensitive API responses
- Sanitize user input before API calls
- Implement proper error boundaries
- Respect rate limits and API quotas

## 📚 Documentation

### Code Documentation

- Add docstrings to all public functions
- Include parameter descriptions and return value info
- Provide usage examples in docstrings
- Explain complex API interactions

### README Updates

- Keep installation instructions current
- Include troubleshooting section
- Document all MCP tools and their parameters
- Provide clear examples for common use cases

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Description** of the issue
2. **Steps to reproduce** the problem
3. **Expected behavior** vs actual behavior
4. **Environment details** (Python version, OS, etc.)
5. **Error messages** or logs (without sensitive data)

## 💡 Feature Requests

When suggesting features:

1. **Describe the use case** and why it would be valuable
2. **Provide examples** of how it would work
3. **Consider the impact** on existing functionality
4. **Be specific** about the requirements

## 🤝 Code Review

### Review Process

- All changes require review before merging
- Address review feedback promptly
- Be respectful and constructive in feedback
- Test changes thoroughly before requesting review

### Review Checklist

- [ ] Code follows style guidelines
- [ ] Tests pass and new tests are added if needed
- [ ] Documentation is updated
- [ ] No sensitive data is committed
- [ ] Changes are backward compatible when possible

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## 🆘 Getting Help

- **GitHub Issues** - For bug reports and feature requests
- **Discussions** - For questions and general discussion
- **Code Review** - For feedback on pull requests

Thank you for contributing to the Codemagic MCP Server! 🎉








