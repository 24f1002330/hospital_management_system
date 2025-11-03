from flask import render_template,request,url_for,redirect
 
def Login(app):
    @app.route('/login',methods=['GET','POST'])
    def login():
        if request.method=='POST':
            email = request.form['e_mail']
            password = request.form['pass_word']

            return redirect(url_for('home'))
        return render_template('login.html')
