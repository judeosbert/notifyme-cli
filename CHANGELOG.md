# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions CI/CD workflows
- Contributing guidelines
- Code of conduct
- Issue and pull request templates
- Security policy

## [1.0.0] - 2024-11-18

### Added
- Initial release of notifyme-cli
- Telegram bot integration for notifications
- Command-line interface with argparse
- Configuration management with JSON storage
- Default message sending without --send flag
- Custom message support with -m/--message flag
- Interactive setup command for bot configuration
- Test command to verify configuration
- Command execution wrapper with --exec flag
- Comprehensive error handling and user feedback
- Unit tests for core functionality
- Example scripts and usage documentation
- MIT license
- Complete README with setup and usage instructions

### Features
- **Simple Usage**: `command && notifyme` sends "Task complete"
- **Custom Messages**: `command && notifyme -m "Custom message"`
- **Configuration**: Secure local storage in ~/.notify-me/config.json
- **Setup**: Interactive `notifyme setup` for easy configuration
- **Testing**: `notifyme test` to verify bot connection
- **Execution Wrapper**: `notifyme --exec command` for timing and exit codes
- **Cross-platform**: Works on macOS, Linux, and Windows
- **Multiple Python versions**: Supports Python 3.8+

### Technical Details
- Configuration read fresh from disk on every notification
- HTTP-based Telegram Bot API integration
- Subprocess execution with timeout and error handling
- Markdown-formatted notification messages
- Duration formatting (seconds, minutes, hours)
- Exit code tracking and reporting
- Comprehensive test coverage

### Development Notes
- Project created with AI assistance (GitHub Copilot)
- Demonstrates modern Python packaging and open-source practices
- Includes comprehensive GitHub workflows and community templates

[Unreleased]: https://github.com/judeosbert/notifyme-cli/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/judeosbert/notifyme-cli/releases/tag/v1.0.0