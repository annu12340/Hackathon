from flask import Flask, render_template, request
from steganography.encode import encode
from utils.image_generation import  generate_new_image
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        message = request.form['message']
        # generate_new_image()
        encode("output", message)
        return render_template('result.html', message=message)
    return render_template('index.html')