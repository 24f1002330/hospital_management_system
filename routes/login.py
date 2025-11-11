from flask import render_template,request,url_for,redirect
from model import *
 
def Login(app):
    @app.route('/login',methods=['GET','POST'])
    def login():
        if request.method=='POST':
            Email = request.form['e_mail']
            Password = request.form['pass_word'] 

            user = Users.query.filter(Users.email == Email) . first()

            if user :
                if user.password == Password :
                    return redirect(url_for('dashboard_patient', user_email = user.email))  # reusing the email variable
                
                else :
                     return render_template("incorrect_login.html")
            else:
                 return render_template ("User_not_found.html")

            return redirect(url_for('home'))
        return render_template('login.html')
