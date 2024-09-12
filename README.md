# GhosttyBot

GhosttyBot is a Discord bot designed specifically for the Ghostty community. Ghostty is a brand new terminal emulator currently in closed beta, and this bot helps manage the frequent requests for beta invites.

## Overview

The bot is built to alleviate the annoying factor on the developer and mod team by automatically handling questions about beta invites in the Discord server. It monitors a specific channel for messages containing the word "invite" and responds with a redirect to the information channel. Planning to add Ollama support to analyze the intent of the users message as sometimes there is a general question about the invite process instead of a request for an invite.

## Setup

1. Clone this repository to your local machine.

2. Copy the `.env-example` file to a new file named `.env`:
   ```
   cp .env-example .env
   ```

3. Open the `.env` file and replace the placeholder values with your actual Discord bot token:
   ```
   DISCORD_BOT_TOKEN=your_bot_token_here
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the bot:
   ```
   python bot.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.