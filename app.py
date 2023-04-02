from flask import Flask,render_template,redirect,url_for,request
from model import recommendor
import auth

app = Flask(__name__)

@app.route('/')
def main():
    return redirect(url_for('login'))

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['pwd']
        if(auth.loginverify(uname,pwd)):
            return redirect(url_for('model'))
    return render_template('login.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        mail = request.form['mail']
        uname = request.form['uname']
        pwd = request.form['pwd']
        if(auth.newuser(mail,uname,pwd)):
            return redirect(url_for('model'))
    return render_template("signup.html")

@app.route('/model',methods=['POST','GET'])
def model():
    if request.method == 'POST':
        mname = request.form['mname']
        recc = recommendor(mname)
        if(type(recc) != bool):
            return render_template("final.html",data=recc)
    return render_template("success.html")

if(__name__ == '__main__'):
    app.run(debug = True)