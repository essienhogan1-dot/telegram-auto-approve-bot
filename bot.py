import os
import logging

from telegram import Update
from telegram.ext import (
    Application,
    ChatJoinRequestHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is missing.")


async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    request = update.chat_join_request

    try:
        await request.approve()

        logging.info(
            f"Approved {request.from_user.full_name} "
            f"({request.from_user.id})"
        )

    except Exception as e:
        logging.error(e)


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(ChatJoinRequestHandler(approve_request))

print("Bot is running...")

app.run_polling(drop_pending_updates=True)