from flask import Flask, render_template, request
from message_encoding.steganography.encode import encode
from message_encoding.utils.image_generation import  generate_new_image
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate_secret_message_encoding():
    if request.method == 'POST':
        message = request.form['message']
        # generate_new_image()
        encode("output", message)
        return render_template('result.html', message=message)
    return render_template('index.html')