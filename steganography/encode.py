from PIL import Image
from steganography.utils import encode_enc

def encode(input_image, message):
    print("---------- Encoding the message -------------")
    img = input_image+".png"
    image = Image.open(img, 'r')

    data = message
    if (len(data) == 0):
        raise ValueError('Data is empty')

    newimg = image.copy()
    encode_enc(newimg, data)

    new_img_name = input_image+"-enc.png"
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
