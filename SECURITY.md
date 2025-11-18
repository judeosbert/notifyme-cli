# Security Policy

## Supported Versions

We actively support and provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please follow these steps:

### 1. Do NOT create a public issue

Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.

### 2. Send a private report

Instead, please send an email to: **[security@yourproject.com]** (replace with actual email)

Include the following information:
- Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit the issue

### 3. What to expect

- **Acknowledgment**: We will acknowledge receipt of your report within 48 hours
- **Investigation**: We will investigate and validate the vulnerability
- **Updates**: We will keep you informed of our progress
- **Resolution**: We will work to resolve the issue as quickly as possible
- **Disclosure**: We will coordinate public disclosure with you

## Security Considerations

### Configuration Storage

- Bot tokens and chat IDs are stored locally in `~/.notify-me/config.json`
- File permissions should be restricted to the user only
- Tokens are never logged or transmitted except to Telegram's API
- Configuration is read fresh from disk on each use

### Network Security

- All communication with Telegram uses HTTPS
- No data is stored on external servers
- Requests include appropriate timeouts to prevent hanging connections

### Input Validation

- Command execution is handled through subprocess with proper argument handling
- Configuration values are validated before use
- Error messages avoid exposing sensitive information

## Best Practices for Users

1. **Protect your bot token**: Never share your bot token publicly
2. **Use dedicated bots**: Create a separate bot for notify-me rather than reusing existing bots
3. **Monitor bot activity**: Check your bot's message history periodically
4. **Secure your chat**: Be aware of who has access to your Telegram chat
5. **Update regularly**: Keep notify-me updated to the latest version

## Scope

This security policy applies to:
- The notify-me Python package
- Configuration management
- Telegram API integration
- Command execution features

## Out of Scope

- Third-party dependencies (report to respective maintainers)
- Telegram's infrastructure or API
- User's local system security
- Issues with user-created commands or scripts

## Security Updates

Security updates will be:
- Released as patch versions (e.g., 1.0.1)
- Announced through GitHub releases
- Documented in the CHANGELOG.md
- Tagged with security labels

## Recognition

We appreciate responsible disclosure and will:
- Credit reporters in our security advisories (unless you prefer to remain anonymous)
- Work with you on coordinated disclosure timing
- Consider your report for our Hall of Fame (if we create one)

## Questions

If you have questions about this security policy, please create a GitHub issue with the "security" label or contact us directly.

---

*This security policy is based on industry best practices and will be updated as needed.*