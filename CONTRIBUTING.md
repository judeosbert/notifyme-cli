# Contributing to notify-me

Thank you for your interest in contributing to notifyme-cli! This document provides guidelines and information for contributors.

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code:

- Be respectful and inclusive
- Focus on what is best for the community
- Show empathy towards other community members
- Be constructive in discussions and feedback

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear description** of the issue
- **Steps to reproduce** the behavior
- **Expected behavior** vs actual behavior
- **Environment details** (OS, Python version, notify-me version)
- **Configuration** (without sensitive tokens)

### Suggesting Features

Feature suggestions are welcome! Please:

1. Check existing feature requests first
2. Clearly describe the feature and use case
3. Explain how it fits with the project's goals
4. Consider if it could be implemented as a plugin or extension

### Development Setup

1. **Fork and clone** the repository:
   ```bash
   git clone https://github.com/judeosbert/notifyme-cli.git
   cd notifyme-cli
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install in development mode**:
   ```bash
   pip install -e ".[dev]"
   ```

4. **Install pre-commit hooks** (optional but recommended):
   ```bash
   pre-commit install
   ```

### Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

2. **Make your changes** following the coding standards below

3. **Add or update tests** for your changes

4. **Run the test suite**:
   ```bash
   make test
   # or
   python -m pytest tests/ -v
   ```

5. **Check code formatting**:
   ```bash
   make lint
   # or
   black --check src/notify_me tests/
   flake8 src/notify_me tests/
   ```

6. **Update documentation** if needed

### Coding Standards

- **Code Style**: Follow PEP 8, enforced by Black formatter
- **Line Length**: Maximum 127 characters (GitHub-friendly)
- **Type Hints**: Use type hints for function parameters and return values
- **Docstrings**: Use Google-style docstrings for functions and classes
- **Imports**: Use absolute imports, group imports logically
- **Error Handling**: Handle errors gracefully with informative messages

### Testing Guidelines

- **Coverage**: Maintain or improve test coverage
- **Unit Tests**: Write focused unit tests for individual functions
- **Integration Tests**: Test feature workflows end-to-end
- **Mock External Services**: Mock Telegram API calls in tests
- **Test Names**: Use descriptive test method names

Example test:
```python
def test_send_notification_success(self, mock_requests):
    """Test successful notification sending."""
    mock_requests.post.return_value.json.return_value = {'ok': True}
    
    notifier = NotifyMe()
    result = notifier.send_notification("test message")
    
    assert result is True
```

### Commit Messages

Use clear, descriptive commit messages:

```
feat: add support for message formatting options
fix: handle network timeouts gracefully  
docs: update installation instructions
test: add tests for configuration validation
refactor: simplify CLI argument parsing
```

### Pull Request Process

1. **Update documentation** for any new features
2. **Add tests** that cover your changes
3. **Ensure CI passes** (tests, linting, formatting)
4. **Update CHANGELOG.md** with your changes
5. **Request review** from maintainers

### Pull Request Template

When creating a PR, please include:

- **Description** of changes made
- **Issue reference** if applicable (Fixes #123)
- **Testing details** - how you tested the changes
- **Breaking changes** if any
- **Screenshots** for UI changes (if applicable)

## Development Commands

The project includes a Makefile with common development tasks:

```bash
make help          # Show available commands
make install       # Install the package
make install-dev   # Install with development dependencies
make test          # Run tests
make test-cov      # Run tests with coverage
make lint          # Run linting
make format        # Format code with black
make clean         # Clean build artifacts
```

## Project Structure

```
notifyme-cli/
├── src/notify_me/          # Main package source
│   ├── cli.py             # Command-line interface
│   ├── config.py          # Configuration management  
│   ├── notifier.py        # Core notification logic
│   └── __init__.py        # Package initialization
├── tests/                  # Test suite
├── examples/              # Usage examples
├── .github/               # GitHub workflows and templates
├── docs/                  # Documentation (if added)
└── setup.py              # Package configuration
```

## Release Process

For maintainers:

1. Update version in `setup.py` and `__init__.py`
2. Update `CHANGELOG.md` with release notes
3. Create and push a git tag: `git tag v1.x.x`
4. Create a GitHub release
5. CI will automatically publish to PyPI

## Getting Help

- **Documentation**: Check the README and code comments
- **Issues**: Search existing issues or create a new one
- **Discussions**: Use GitHub Discussions for questions
- **Contact**: Reach out to maintainers for urgent matters

## Recognition

Contributors will be recognized in:
- CHANGELOG.md for their contributions
- GitHub contributors page
- Release notes for significant contributions

## About This Project

This project was initially created with AI assistance (GitHub Copilot) as a demonstration of modern Python development practices. We welcome human contributors to help improve and expand the functionality!

Thank you for contributing to notifyme-cli! 🎉