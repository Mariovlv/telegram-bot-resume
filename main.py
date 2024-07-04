import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from controllers.start_controller import start, help_command
from controllers.news_controller import news_command, handle_article_selection
from controllers.settings_controller import settings_command, handle_setting_selection, handle_setting_change

load_dotenv()

def main() -> None:
    application = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("news", news_command))
    application.add_handler(CommandHandler("settings", settings_command))
    application.add_handler(CallbackQueryHandler(button_callback))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

async def button_callback(update, context) -> None:
    query = update.callback_query
    if query.data.startswith("article_"):
        await handle_article_selection(query, context)
    elif query.data.startswith("set_"):
        await handle_setting_selection(query, context)
    else:
        await handle_setting_change(query, context)

if __name__ == "__main__":
    main()