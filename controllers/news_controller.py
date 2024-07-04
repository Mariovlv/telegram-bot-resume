from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from helpers.news_helpers import get_news
from helpers.settings_helpers import DEFAULT_SETTINGS

async def news_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    settings = context.user_data.get('settings', DEFAULT_SETTINGS.copy())
    articles = await get_news(settings)
    
    if not articles:
        await update.message.reply_text("Sorry, no news articles found. Try changing your settings with /settings.")
        return

    keyboard = []
    for i, article in enumerate(articles):
        keyboard.append([InlineKeyboardButton(article['title'][:40] + "...", callback_data=f"article_{i}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Select a news headline:", reply_markup=reply_markup)
    context.user_data['articles'] = articles

async def handle_article_selection(query, context):
    article_index = int(query.data.split("_")[1])
    article = context.user_data['articles'][article_index]
    message = f"Title: {article['title']}\n\n"
    message += f"Description: {article.get('description', 'No description available')}\n\n"
    message += f"Content: {article.get('content', 'No content available')}\n\n"
    message += f"Read more: {article['url']}"

    await context.bot.delete_message(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id
    )

    await context.bot.send_message(
        chat_id=query.message.chat_id,
        text=message
    )

    await context.bot.send_message(
        chat_id=query.message.chat_id,
        text="You can use /news again to see more headlines or /settings to change preferences."
    )

    await query.answer()