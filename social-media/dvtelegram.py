import logging
from PIL import Image
from io import BytesIO
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

group_chat_id = -1002111911039
personal_chat_id = -1

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
    if update.message.chat.id == group_chat_id:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Image detected!")
        
        # Steganography
        if update.message.photo:
            print('photoooo')
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
    default_message = "Name: Lydia Davis, Phone: 1234567, Please help me. I am at the SW library"

    # TODO: Steganography
    message = ""
    return message if message else default_message


if __name__ == '__main__':
    application = ApplicationBuilder().token('7148403045:AAGjgCm2qMhGB8FoFgd7SLx8UXa5zUuozOw').build()
    
    start_handler = CommandHandler('start', start)
    msg_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), msgHandler)
    image_handler = MessageHandler(filters.PHOTO, photoHandler)

    # application.add_handler(start_handler)
    application.add_handler(msg_handler)
    application.add_handler(image_handler)
    
    
    application.run_polling()