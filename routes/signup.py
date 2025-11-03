from flask import render_template,request

def Signup(app):
    @app.route('/signup_patient', methods = ['GET','POST'])
    def signup_patient():
         if request.method == 'POST':
              Username = request.form['user_name']
              Email = request.form['e_mail']
              Password = request.form['pass_word']

         return render_template('signup_patient.html')
            
                