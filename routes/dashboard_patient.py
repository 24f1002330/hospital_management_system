from flask import render_template,request 
from model import *

def Dashboard_patient(app):

          @app.route('/dashboard_patient/<user_email>', methods = ['GET','POST'])
          def dashboard_patient(user_email):
                      user = Users.query.filter(Users.email == user_email).first()
                      departments = Departments.query.all()
                      if user:
                              return render_template('dashboard_patient.html', user = user , departments = departments)
                      else:
                           return "User not found"
         
              
