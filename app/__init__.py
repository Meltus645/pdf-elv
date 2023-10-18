from pathlib import Path
from .models import User
from .utils.dbconf import db
from flask import Flask, render_template, request, redirect, url_for, session, flash

def create_app(config:dict =None):
    BASEDIR =Path(__file__).resolve().parent.parent
    app =Flask(__name__, template_folder=BASEDIR /'templates', static_folder=BASEDIR /'static')

    # config app
    if config: app.config.from_object(config)
    else: app.config.from_pyfile(BASEDIR /'config.py')

    # db
    db.init_app(app)

    # Signup Page
    @app.route('/', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            cpassword=request.form['cpassword']
            pnnumber=request.form['pnnumber']
            email=request.form['email']
            hyu=request.form['who']
            # if password == cpassword:
            #     cursor = db.cursor()
            #     cursor.execute("INSERT INTO users (username,email,pnnumber,hcdu,password) VALUES (%s, %s,%s,%s,%s)", (username,email,pnnumber,hyu,password))
            #     db.commit()
            #     cursor.close()
            #     flash('1')
                
            # else:
            #     flash('2')
                
            # return render_template('./signup.html')
            print(request.form)
        return render_template('./signup.html')
    # Login Page
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            # cursor = db.cursor()
            # cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password ='{password}'")
            # user = cursor.fetchall()
            ##print(user[0][1])
            # cursor.close()  # Close the cursor after fetching the result
            # if user:
            #     session['username'] = user[0][1]
            #     session['userid'] = user[0][0]
            #     session['email']=user[0][2]
            #     receiver_email=session['email']
            #     user_name=session['username']
                # send_mail(receiver_email,user_name)
            #     flash('Login successful!')
            #     return render_template('pdf_upload.html',username=username,pdfimage={},pdffont={})
            # else:
            #     flash('wrong') 
        return render_template('login.html')

    return app