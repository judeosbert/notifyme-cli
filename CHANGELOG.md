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
- Initial release of notify-me
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
- **Simple Usage**: `command && notify-me` sends "Task complete"
- **Custom Messages**: `command && notify-me -m "Custom message"`
- **Configuration**: Secure local storage in ~/.notify-me/config.json
- **Setup**: Interactive `notify-me setup` for easy configuration
- **Testing**: `notify-me test` to verify bot connection
- **Execution Wrapper**: `notify-me --exec command` for timing and exit codes
- **Cross-platform**: Works on macOS, Linux, and Windows
- **Multiple Python versions**: Supports Python 3.7+

### Technical Details
- Configuration read fresh from disk on every notification
- HTTP-based Telegram Bot API integration
- Subprocess execution with timeout and error handling
- Markdown-formatted notification messages
- Duration formatting (seconds, minutes, hours)
- Exit code tracking and reporting
- Comprehensive test coverage

[Unreleased]: https://github.com/yourusername/notify-me/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/yourusername/notify-me/releases/tag/v1.0.0