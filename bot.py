import os
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# BOT TOKEN and ESP URL (DO NOT hardcode — Use Railway Variables)
TOKEN = os.environ.get("TOKEN")
ESP_URL = os.environ.get("ESP_URL")  # Example: http://192.168.0.101

def turn_on(update, context):
    requests.get(f"{ESP_URL}/led/on")
    update.message.reply_text("LED turned ON")

def turn_off(update, context):
    requests.get(f"{ESP_URL}/led/off")
    update.message.reply_text("LED turned OFF")

def voice_or_text(update, context):
    text = update.message.text.lower()
    if "on" in text:
        turn_on(update, context)
    elif "off" in text:
        turn_off(update, context)
    else:
        update.message.reply_text("Say 'on' or 'off'.")

def start(update, context):
    update.message.reply_text("Bot is online and ready!")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, voice_or_text))

updater.start_polling()
updater.idle()
