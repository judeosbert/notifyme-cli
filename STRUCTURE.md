# notify-me Project Structure

This project provides a complete command-line notification system using Telegram webhooks.

## Project Structure

```
notify-me/
├── src/
│   └── notify_me/
│       ├── __init__.py          # Package initialization
│       ├── cli.py               # Command-line interface
│       ├── config.py            # Configuration management
│       └── notifier.py          # Core notification functionality
├── tests/
│   ├── __init__.py
│   └── test_notify_me.py        # Unit tests
├── examples/
│   ├── example_task.py          # Example Python script
│   └── backup_script.sh         # Example shell script
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup configuration
├── README.md                    # Project documentation
├── LICENSE                      # MIT license
├── .gitignore                   # Git ignore rules
└── Makefile                     # Development commands
```

## Key Features Implemented

1. **Command-line Interface**: Full argparse-based CLI with subcommands
2. **Configuration Management**: JSON-based config storage in ~/.notify-me/
3. **Telegram Integration**: HTTP API calls to Telegram bot webhook
4. **Command Execution**: Subprocess wrapper with timing and exit code tracking
5. **Error Handling**: Comprehensive error handling and user feedback
6. **Testing**: Unit tests for core functionality
7. **Documentation**: Complete README with setup and usage instructions

## Installation and Usage

1. Install: `pip install -e .`
2. Setup: `notify-me setup` (enter bot token and chat ID)
3. Test: `notify-me test`
4. Use: `notify-me -m "Custom message" your-command-here`

## Example Commands

```bash
# Set up the bot
notify-me setup

# Test configuration
notify-me test

# Run with notification
notify-me python examples/example_task.py
notify-me -m "Backup complete" bash examples/backup_script.sh

# Send direct message
notify-me --message "Hello from CLI!" --send
```