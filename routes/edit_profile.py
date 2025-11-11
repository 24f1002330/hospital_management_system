from flask import render_template,request,url_for,redirect,flash
from model import * 
from datetime import date

def Edit_profile(app):
         @app.route('/edit_profile/<user_email>' , methods = ['GET','POST'])
         
         def edit_profile(user_email):
                   user = Users.query.filter(Users.email == user_email).first()
                   
                   
                   if request.method == 'POST':
                          user.username = request.form['user_name']
                          user.email = request.form['e_mail']
                          user.phoneno = request.form['phone_no']

                          dob_str = request.form.get('d_ob')
                          user.dob = date.fromisoformat(dob_str) if dob_str else None

                          
                          db.session.commit() 

                          return redirect(url_for('dashboard_patient',user_email = user.email))
    
                   return render_template('edit_profile.html', user = user)

