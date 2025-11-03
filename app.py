from flask import Flask,render_template,request
#from routes.login import Login
from routes.signup import Signup
import os

app=Flask(__name__)

@app.route('/',methods = ['GET'])

def home():
    return render_template('landingpage.html')

#Login(app)
Signup(app)

if __name__ == "__main__":
      app.debug = True
      app.run(host = '0.0.0.0', port = 3000)
       
