import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there!")
        
async def msgHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    


if __name__ == '__main__':
    application = ApplicationBuilder().token('7148403045:AAGjgCm2qMhGB8FoFgd7SLx8UXa5zUuozOw').build()
    
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), msgHandler)

    # application.add_handler(start_handler)
    application.add_handler(echo_handler)
    
    application.run_polling()