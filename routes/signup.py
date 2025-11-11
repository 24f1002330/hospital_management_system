from flask import render_template,request
from model import *

def Signup(app):
    @app.route('/signup_patient', methods = ['GET','POST'])
    def signup_patient():
         if request.method == 'POST':
              Username = request.form['user_name']
              Email = request.form['e_mail']
              Password = request.form['pass_word']

              existing_user =  Users.query.filter(Users.email == Email).first()

              if existing_user:
                       return render_template("incorrect_signup.html")
                   
              
              new_user=Users(
                             username = Username,
                             email = Email,
                             password = Password,
                             
                            )
              
              db.session.add(new_user)
              db.session.commit()

              return render_template("landingpage.html")



         return render_template('signup_patient.html')
            
                