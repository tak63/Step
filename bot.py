from telegram import Bot
import os

# توکن بات تلگرام خود را اینجا وارد کنید
TOKEN = 'YOUR_BOT_TOKEN'
bot = Bot(token=TOKEN)

# ارسال یک پیام ساده
bot.send_message(chat_id='YOUR_CHAT_ID', text="سلام! این یک پیام تست از بات تلگرام است.")
