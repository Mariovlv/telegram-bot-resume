import asyncio
import requests
from datetime import date, timedelta
import os

def generate_url(settings):
    today_day_formatted = date.today() - timedelta(days=1)
    news_key = os.getenv("NEWS_API_KEY")
    url_get_news = f"https://newsapi.org/v2/top-headlines?country={settings['country']}&category={settings['category']}&from={today_day_formatted}&sortBy=popularity&apiKey={news_key}"
    return url_get_news

async def get_news(settings):
    url_get_news = generate_url(settings)
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url_get_news)
    articles = response.json()
    return articles.get('articles', [])[:15]  # Return only the first 15 articles, or empty list if no articles