from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

updater = Updater(token='1545195878:AAFpbdvUwBEolXmbi4Srr4Np3cUOh5bTrhc')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуй, братан!")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text[::-1])
echo_handler = MessageHandler(Filters.text,echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()