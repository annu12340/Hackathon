from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome page"

@app.route('/generate', methods=['GET', 'POST'])
def generate_image():
    if request.method == 'POST':
        message = request.form['message']

        return render_template('result.html', message=message)
    return render_template('index.html')