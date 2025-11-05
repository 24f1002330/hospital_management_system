from flask import Flask,render_template,request
from routes.login import Login
from routes.signup import Signup
import os
from model import *

current_dir = os.path.abspath(os.path.dirname(__file__))


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(current_dir,'database.sqlite3')
db.init_app(app)
app.app_context().push()


@app.route('/',methods = ['GET'])

def home():
    return render_template('landingpage.html')

Login(app)
Signup(app)

if __name__ == "__main__":
      db.create_all()
      app.debug = True
      app.run(host = '0.0.0.0', port = 3000)
       
