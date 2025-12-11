from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

BOT_TOKEN = "7582354157:AAFjVCPdhklnoUbPpcI9LATBSxj5VnED5TY"

def start(update, context):
    update.message.reply_text("Bot is Running!")

def echo(update, context):
    msg = update.message.text.lower()
    if msg == "on":
        update.message.reply_text("Turning LED ON")
    elif msg == "off":
        update.message.reply_text("Turning LED OFF")
    else:
        update.message.reply_text("Unknown command")

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()
