# notify-me

[![CI](https://github.com/yourusername/notify-me/workflows/CI/badge.svg)](https://github.com/yourusername/notify-me/actions)
[![PyPI version](https://badge.fury.io/py/notify-me.svg)](https://badge.fury.io/py/notify-me)
[![Python versions](https://img.shields.io/pypi/pyversions/notify-me.svg)](https://pypi.org/project/notify-me/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/yourusername/notify-me/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/notify-me)

A command-line tool that sends Telegram notifications when long-running commands complete. Never miss when your builds, tests, or data processing jobs finish!

## ✨ Features

- 🔔 Get notified via Telegram when commands finish
- ⏱️ Shows command duration and exit status
- 📝 Add custom messages to notifications
- 🛠️ Easy setup with interactive configuration
- 🎯 Works with any command-line program
- 💾 Secure local configuration storage

## 📦 Installation

### From PyPI (Recommended)
```bash
pip install notify-me
```

### From Source
```bash
git clone https://github.com/yourusername/notify-me.git
cd notify-me
pip install -e .
```

### Development Installation
```bash
git clone https://github.com/yourusername/notify-me.git
cd notify-me
pip install -e ".[dev]"
```

## Setup

### 1. Create a Telegram Bot

1. Open Telegram and message [@BotFather](https://t.me/botfather)
2. Send `/newbot` and follow the instructions
3. Save the bot token you receive

### 2. Get Your Chat ID

1. Message [@userinfobot](https://t.me/userinfobot) on Telegram
2. It will reply with your user information including your chat ID
3. Save the chat ID (it's a number like `123456789`)

### 3. Configure notify-me

Run the setup command and enter your bot token and chat ID:

```bash
notify-me setup
```

The setup will test the connection and confirm everything works.

## Usage

### Basic Usage (Recommended)

Run commands and then notify when complete:
```bash
# Send default "Task complete" message
python train_model.py && notify-me

# Send custom message
make build && notify-me -m "Build finished"

# Chain multiple commands
npm test && npm build && notify-me -m "CI pipeline complete"
```

### Direct Message Sending

Send a message directly:
```bash
notify-me                                    # Send "Task complete"
notify-me -m "Hello from the command line!"  # Send custom message
```

### Command Wrapper (Alternative)

Execute commands with notification wrapper:
```bash
notify-me --exec python train_model.py
notify-me --exec -m "Training complete!" python train_model.py
```

### Test Configuration

Test your setup:
```bash
notify-me test
```

## Command Examples

```bash
# Long-running build with notification (recommended)
docker build -t myapp . && notify-me -m "Docker build complete"

# Database backup with notification
pg_dump mydatabase > backup.sql && notify-me -m "Backup finished"

# Machine learning training
python train.py --epochs 100 && notify-me -m "Model training done"

# Run tests and get notified
pytest tests/ && notify-me

# Complex pipeline
bash ./process_data.sh && notify-me -m "Data processing complete"

# Using the wrapper (alternative method)
notify-me --exec pytest tests/
notify-me --exec -m "Training complete!" python train.py
```

## Configuration

Configuration is stored in `~/.notify-me/config.json`. The file contains:

```json
{
  "bot_token": "your-bot-token-here",
  "chat_id": "your-chat-id-here"
}
```

## Security

- Your bot token and chat ID are stored locally on your machine
- No data is sent to external servers except Telegram's API
- Configuration file has restricted permissions (600)

## Notification Format

Notifications include:
- ✅/❌ Success or failure status
- Command that was executed
- Execution time
- Timestamp
- Custom message (if provided)
- Exit code (if command failed)

Example notification:
```
✅ Command completed successfully

Message: Training finished!

Command: python train_model.py
Duration: 2.3 hours
Time: 2024-11-17 14:30:22
```

## Troubleshooting

### "Bot not configured" Error
Run `notify-me setup` to configure your bot token and chat ID.

### "Connection error" or timeout
- Check your internet connection
- Verify your bot token is correct
- Make sure your bot hasn't been deleted

### "Telegram API error"
- Verify your chat ID is correct
- Make sure you've sent at least one message to your bot
- Check that your bot token is valid

### Permission errors
The configuration directory `~/.notify-me/` should be writable by your user.

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Installing for Development
```bash
pip install -e ".[dev]"
```

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if needed
5. Submit a pull request

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Start for Contributors

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Run tests: `make test`
5. Submit a pull request

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⭐ Support

If you find this project helpful, please consider:
- Giving it a star on GitHub ⭐
- Reporting bugs or requesting features through [issues](https://github.com/yourusername/notify-me/issues)
- Contributing to the codebase
- Sharing it with others who might find it useful

## 🔗 Links

- [PyPI Package](https://pypi.org/project/notify-me/)
- [GitHub Repository](https://github.com/yourusername/notify-me)
- [Documentation](https://github.com/yourusername/notify-me#readme)
- [Issue Tracker](https://github.com/yourusername/notify-me/issues)
- [Discussions](https://github.com/yourusername/notify-me/discussions)