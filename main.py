from flask import Flask, render_template, request
from steganography.encode import encode

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome page"

@app.route('/generate', methods=['GET', 'POST'])
def generate_image():
    if request.method == 'POST':
        message = request.form['message']
        encode("test", message)
        return render_template('result.html', message=message)
    return render_template('index.html')