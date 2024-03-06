import logging
import os

from telegram import Update, ext
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

# import cv2  # Import OpenCV library
# import pytesseract  # Import Tesseract library (for text recognition)


# Replace with your Telegram bot's API token
TELEGRAM_BOT_TOKEN = "7148403045:AAGjgCm2qMhGB8FoFgd7SLx8UXa5zUuozOw"

# Configure Tesseract path (if not installed globally)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Replace with your Tesseract installation path

def handle_image(update: Update, context: ext.CallbackContext):
    chat_id = update.effective_chat.id

    if not update.message.photo:
        # Handle cases where no image is sent (e.g., text message)
        context.bot.send_message(chat_id=chat_id, text="Please send an image to be processed.")
        return

    try:
        file_id = update.message.photo[-1].file_id
    except IndexError:
        # Handle cases where the photo list is empty
        context.bot.send_message(chat_id=chat_id, text="An error occurred while processing the image.")
        return

    # ... (rest of the image processing logic remains the same)

def main():
    application = ApplicationBuilder().token('7148403045:AAGjgCm2qMhGB8FoFgd7SLx8UXa5zUuozOw').build()
    
    application.add_handler(MessageHandler(filters.Document.IMAGE, handle_image))
    
    
    application.run_polling()

if __name__ == '__main__':
    main()
