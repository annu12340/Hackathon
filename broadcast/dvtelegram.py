import logging
import requests
from faker import Faker
from PIL import Image
from io import BytesIO
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there!")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
        
async def msgHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    
async def photoHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Image detected!")
    
    # Steganography
    if update.message.photo:
        # Get the file ID of the image
        file_id = update.message.photo[-1].file_id
        # Get the image file
        image_file = await context.bot.get_file(file_id)
        # Download the image
        image_bytes = await image_file.download_as_bytearray()

        # Perform steganography
        message = extract_message_from_image(image_bytes)

        # Send the extracted message as a response
        await context.bot.send_message(chat_id=update.message.chat_id, text=message)

def extract_message_from_image(image_bytes):
    faker = Faker('en_US')  # Set the locale to US English
    default_message = f"Name: {faker.first_name_female()}, Phone: {faker.phone_number()}, Please help me. I am at the {faker.address()}"

    # TODO: Steganography functionality here
    message = ""
    
    add_to_convex_db(default_message)
    
    return message if message else default_message

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
    application = ApplicationBuilder().token('7148403045:AAGjgCm2qMhGB8FoFgd7SLx8UXa5zUuozOw').build()
    
    start_handler = CommandHandler('start', start)
    msg_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), msgHandler)
    image_handler = MessageHandler(filters.PHOTO, photoHandler)

    # application.add_handler(start_handler)
    application.add_handler(msg_handler)
    application.add_handler(image_handler)
    
    
    application.run_polling()