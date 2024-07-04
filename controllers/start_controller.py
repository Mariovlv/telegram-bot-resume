from telegram import Update
from telegram.ext import ContextTypes
from helpers.settings_helpers import DEFAULT_SETTINGS

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    context.user_data.setdefault('settings', DEFAULT_SETTINGS.copy())
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Use /news to get the latest news or /settings to change preferences."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Use /news to get the latest news headlines and /settings to change preferences.")