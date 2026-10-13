# 🤖 Telegram Auto Approval Bot

A simple Telegram bot that automatically approves all join requests to a private Telegram channel.

## Features

- ✅ Automatically approves all join requests
- ✅ Works with private Telegram channels
- ✅ Easy deployment on Railway
- ✅ Lightweight and fast
- ✅ Built with Python and python-telegram-bot

---

## Requirements

- Python 3.12+
- A Telegram Bot created with BotFather
- A private Telegram channel
- Railway account (or another Python hosting platform)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/telegram-auto-approve-bot.git
cd telegram-auto-approve-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create your environment file

Rename:

```text
.env.example
```

to

```text
.env
```

Then add your BotFather token:

```env
BOT_TOKEN=YOUR_BOT_TOKEN_HERE
```

---

## Running Locally

```bash
python bot.py
```

If everything is configured correctly, you'll see:

```text
Bot is running...
```

---

## Railway Deployment

1. Push the project to GitHub.
2. Create a new Railway project.
3. Select **Deploy from GitHub**.
4. Choose your repository.
5. Add an environment variable:

```
BOT_TOKEN=YOUR_BOT_TOKEN
```

6. Railway will automatically deploy your bot.

---

## Telegram Setup

1. Create a private Telegram channel.
2. Add your bot as an administrator.
3. Enable **Manage Join Requests** permission.
4. Create an invite link with **Request Admin Approval** enabled.
5. Share the invite link with users.

The bot will automatically approve every new join request.

---

## Project Structure

```text
telegram-auto-approve-bot/
│── bot.py
│── requirements.txt
│── runtime.txt
│── railway.json
│── Procfile
│── .env.example
│── .gitignore
└── README.md
```

---

## License

This project is free to use and modify.

---

## Author

Developed using Python and the Telegram Bot API.