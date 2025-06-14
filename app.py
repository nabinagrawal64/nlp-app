# it is server side rendering
from flask import Flask, render_template
from flask import request, redirect, session
from db import Database
import api
import os
from dotenv import load_dotenv

app = Flask(__name__)
dbo = Database()
load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")

# home page
@app.route('/')
def index():
    return render_template('login.html')


# register route
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform-registration', methods=['POST'])
def perform_registration():
    name = request.form.get('full_name')
    email = request.form.get('email')
    password = request.form.get('password')
    # print(name, email, password)

    response = dbo.insert(name, email, password)    
    if response:
        return render_template('login.html', message="Registration successful! You can now log in.")
    else:   
        return render_template('register.html', message="Registration failed. Please try again.")


# login route
@app.route('/perform-login', methods=['POST'])
def perform_login():
    email = request.form.get('email')
    password = request.form.get('password')
    # print(email, password)

    response = dbo.search(email, password) 
    if response['status'] == 'success':
        session['name'] = response['name']
        return redirect('/profile')
    else:
        return render_template('login.html', message="Incorrect email or password")


# profile route
@app.route('/profile')
def profile():
    if 'name' in session:
        return render_template('profile.html')
    else:
        # If user is not logged in, redirect to login page
        return redirect("/")


# NER route
@app.route('/ner')
def ner():
    if 'name' in session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform-ner', methods=['POST'])
def perform_ner():
    if 'name' in session:
        text = request.form.get('text')
        response = api.ner(text)
        # print(response)

        return render_template('ner.html', response=response)
    else:
        return redirect("/")


# logout route
@app.route('/logout')
def logout():
    session.clear()  # clears the entire session
    return redirect('/')



app.run(debug=True, port=3000)



