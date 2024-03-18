import requests, os
from steganography.decode import decode
from PIL import Image
from io import BytesIO
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler


def has_substring(string, substring):
    return substring in string

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there!")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def msgHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)

async def photoHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message)

    # Steganography
    if update.message.photo:
        capture = "#staywoke"
        caption = update.message.caption
        if caption is not None and caption.strip() != "" and has_substring(caption, capture):
            # Get the file ID of the image
            file_id = update.message.photo[-1].file_id
            # Get the image file
            image_file = await context.bot.get_file(file_id)
            # Download the image
            image_bytes = await image_file.download_as_bytearray()

            # Perform steganography
            message = decode(image_bytes)
            return message



def add_to_convex_db(message):
    url = "https://tame-scorpion-381.convex.cloud/api/mutation"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "path": "messages:send",
        "args": {"message": message, "status": "new"},
        "format": "json"
    }
    response = requests.post(url, json=data, headers=headers)
    print(f"Convex response: {response.text}")


if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()

    start_handler = CommandHandler('start', start)
    msg_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), msgHandler)
    image_handler = MessageHandler(filters.PHOTO, photoHandler)

    # application.add_handler(start_handler)
    application.add_handler(msg_handler)
    application.add_handler(image_handler)


    application.run_polling()