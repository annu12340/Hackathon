from telegram.ext import Updater, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
updater = Updater(token='7148403045:AAGjgCm2qMhGB8FoFgd7SLx8UXa5zUuozOw', use_context=True)
dispatcher = updater.dispatcher

def handle_message(update, context):
    if update.message.text:
        action_a(update, context)
    elif update.message.photo:
        action_b(update, context)

def action_a(update, context):
    # Action A: Do something with text messages
    context.bot.send_message(chat_id=update.message.chat_id, text="Received a text message.")

def action_b(update, context):
    # Action B: Do something with images
    context.bot.send_message(chat_id=update.message.chat_id, text="Received an image.")

message_handler = MessageHandler(Filters.all, handle_message)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
