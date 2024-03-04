from flask import Flask, render_template, request
from models import db, UserInfo

from message_encoding.steganography.encode import encode
from message_encoding.utils.image_generation import  generate_new_image

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_info.db'
db.init_app(app)

# ---- Starting page of the site -----
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


# ---- Saving user info -----
@app.route('/info', methods=['GET', 'POST'])
def get_user_info():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        blood_group = request.form['blood_group']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']

        user_info = UserInfo(name=name, age=age, blood_group=blood_group, address=address, city=city, state=state, zip_code=zip_code)
        db.session.add(user_info)
        db.session.commit()

        return 'User information saved successfully!'
    return render_template('get_user_info.html')

# ---- Perform stenographic encoding of the message-----
@app.route('/generate', methods=['GET', 'POST'])
def generate_secret_message_encoding():
    if request.method == 'POST':
        message = request.form['message']
        # generate_new_image()
        encode("output", message)
        return render_template('result.html', message=message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()