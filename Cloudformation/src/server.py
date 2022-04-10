from flask import Flask,render_template,request,redirect, flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'secretkey'


def debugHelp(message = ""):
    print("\n\n-----------------------", message, "--------------------")
    print('REQUEST.FORM:', request.form)
    print('SESSION:', session)

@app.route('/')
def index():
    debugHelp("root")
    return render_template('index.htm')

@app.route('/register', methods = ['POST'])
def verify():
    session['email'] = request.form['email']
    session['firstname'] = request.form['firstname']
    session['lastname'] = request.form['lastname']
    session['password1'] = request.form['password1']
    session['password2'] = request.form['password2']

    if len (session['firstname']) < 1:
        flash ("Name cannot be blank")
    
    if (request.form['firstname'].isdigit() == True):
        print (request.form['firstname'].isdigit())
        flash ("Name cannot contain any numbers")
    
    if len (session['lastname']) < 1:
        flash ("The last name cannot be blank")

    if not EMAIL_REGEX.match (request.form['email']):
        flash ("Invalid email address")

    if request.form['password1'] != request.form['password2']:
        flash ("Passwords do not match!")

    if len (request.form['password1']) < 8:
        flash ("Must be at least 8 characters long")

    if len (request.form['password2']) < 8:
        flash ("Must be at least 8 characters long")
 
    debugHelp("Register")
    return redirect('/')
    
@app.route('/process', methods = ['POST'])
def show_user():

    debugHelp("Register")
    return render_template('submitted.htm')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
