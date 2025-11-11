from flask import Flask,render_template,request
#from routes.login import Login
from routes.signup import Signup
from routes.login import Login
from routes.dashboard_patient import Dashboard_patient
from routes.edit_profile import Edit_profile
import os
from model import *
#from routes.login import Login
#from routes.signup import Signup

current_dir = os.path.abspath(os.path.dirname(__file__))


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(current_dir,'database.sqlite3')
db.init_app(app)
app.app_context().push()

def hosp_departments():
     departments = [
          "Cardiology",
        "Paediatrics",
        "Orthopaedics",
        "Neurology",
        "Urology",
        "Gynaecology",
        "ENT",
        "Opthalmology"
    ]
      
     for dept_name in departments:
            dept = Departments.query.filter(Departments.name == dept_name).first()
            if not dept:
                     newdept = Departments(
                           name = dept_name
                     )

                     db.session.add(newdept)
                    
     db.session.commit()
           


@app.route('/',methods = ['GET'])

def home():
    return render_template('landingpage.html')

Login(app)
Signup(app)
Dashboard_patient(app)
Edit_profile(app)

if __name__ == "__main__":
     
      app.debug = True
      db.create_all()
      hosp_departments()
      app.run(host = '0.0.0.0', port = 3000)
       
