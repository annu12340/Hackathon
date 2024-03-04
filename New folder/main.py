from flask import Flask, render_template, request
from flask_migrate import Migrate, migrate
 
# from models import db, UserInfo

from message_encoding.steganography.encode import encode
from message_encoding.utils.image_generation import  generate_new_image
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = 'the random string'
db = SQLAlchemy(app)

# Settings for migrations
migrate = Migrate(app, db)

#################### All the databases ################################
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    typeOfAccount = db.Column(db.String(10))
    credentials = db.Column(db.String(50))
    image = db.Column(db.String(50))
    about = db.Column(db.String(50))
    skills = db.Column(db.String(50))
    institute = db.Column(db.String(50))
    verifiedskills = db.Column(db.String(50))
    github = db.Column(db.String(50))
    linkedin = db.Column(db.String(50))
    score = db.Column(db.Integer, default=100)

# Define UserInfo model
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    blood_group = db.Column(db.String(5))
    address = db.Column(db.String(200))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    zip_code = db.Column(db.String(10))

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_user = User(username=request.form['username'],
                        password=request.form['password'], typeOfAccount=request.form['typeOfAccount'],
                        credentials=request.form['credentials'], institute=request.form['institute'],
                        skills=request.form['skills'], image=request.form['image'], about=request.form['about'],
                        github=request.form['github'], linkedin=request.form['linkedin'])

        db.session.add(new_user)
        db.session.commit()
        return "prrrr"
    return render_template('register.html')

# ---- Starting page of the site -----
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

# ---- Saving user info -----
@app.route('/info', methods=['GET', 'POST'])
def get_user_info():
    if request.method == 'POST':
        print("hooooo")
        name = request.form['name']
        age = request.form['age']
        blood_group = request.form['blood_group']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        print("1111")
        user_info = UserInfo(name=name, age=age, blood_group=blood_group, address=address, city=city, state=state, zip_code=zip_code)
        print("2222")
        db.session.add(user_info)
        print("3333")
        db.session.commit()
        print("saved")

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
    app.run(debug=True)