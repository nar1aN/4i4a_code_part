import os
from dotenv import load_dotenv
#переменные из .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Нет BOT_TOKEN в .env")