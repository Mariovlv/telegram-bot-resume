# telegram-resume-bot

NewsSum Bot is a Telegram bot that delivers summarized news articles to users. It fetches recent news and uses Google Cloud's Natural Language API to create concise summaries.

## Features

- Fetches the latest news articles
- Summarizes articles using natural language processing
- Delivers summaries directly through Telegram
- Project powered by [echobot.py](https://docs.python-telegram-bot.org/en/v21.3/examples.echobot.html)

## Prerequisites

- Python 3.7+
- A Telegram Bot Token
- Google Cloud account with Natural Language API enabled
- News API key (e.g., NewsAPI)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Mariovlv/telegram-bot-resume
   cd newssum-bot
   ```

2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - `TELEGRAM_BOT_TOKEN`: Your Telegram Bot Token
   - `NEWS_API_KEY`: Your News API Key
   - `GOOGLE_APPLICATION_CREDENTIALS`: Path to your Google Cloud service account key JSON file

## Usage

1. Run the bot:

   ```bash
   python3 bot.py
   ```

2. In Telegram, start a chat with your bot and use the following commands:
   - `/start`: Initializes the bot
   - `/news`: Fetches and summarizes the latest news article
   - `/settings`: Changes the country and category
