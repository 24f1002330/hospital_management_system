from flask import render_template,request,url_for,redirect
from model import *
 
def Login(app):
    @app.route('/login',methods=['GET','POST'])
    def login():
        if request.method=='POST':
            email = request.form['e_mail']
            password = request.form['pass_word'] 

            user = Users.query.filter(Users.email == email) . first()

            if user :
                if user.password == password :
                    return "User found"
                
                else :
                    return " Incorrect Password"
            else:
                return "User not found"

            return redirect(url_for('home'))
        return render_template('login.html')
