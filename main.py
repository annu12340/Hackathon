from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome page"

@app.route("/generate")
def generate_image():
    return "Welcome page"