from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from helpers.settings_helpers import DEFAULT_SETTINGS

async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Country", callback_data="set_country")],
        [InlineKeyboardButton("Category", callback_data="set_category")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose a setting to change:", reply_markup=reply_markup)

async def handle_setting_selection(query, context):
    setting = query.data.split("_")[1]
    options = {
        "country": ["us", "mx", "de", "ar", "gb"],
        "category": ["general", "science", "technology", "business", "health", "sports", "entertainment"]
    }
    keyboard = [[InlineKeyboardButton(option, callback_data=f"{setting}_{option}") for option in options[setting]]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(f"Select {setting}:", reply_markup=reply_markup)

async def handle_setting_change(query, context):
    setting, value = query.data.split("_")
    context.user_data.setdefault('settings', DEFAULT_SETTINGS.copy())
    context.user_data['settings'][setting] = value
    await query.edit_message_text(f"{setting.capitalize()} has been set to {value}. Use /news to get news with new settings.")