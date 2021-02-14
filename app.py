from flask import Flask,session,render_template,redirect,request,url_for
import db as api
import credential
import mailing as mail
from itsdangerous import URLSafeTimedSerializer,SignatureExpired


app = Flask(__name__)
app.secret_key=credential.secret_key

s = URLSafeTimedSerializer(credential.secret_key)


@app.route('/')
def home():
    if 'email' in session:
        email=session['email']
        return render_template('index.html')
    return render_template('signup.html')


@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=='POST':
        form_details=request.form
        if form_details['pass']==from_details['re_pass']:
            email=form_details['email']
            # print(email,"hehehehehheheheh")
            token = s.dumps(email,salt='email-confirm')
            link = url_for('confirm_email',token=token,_external=True)
            msg = 'This link will disable in 10 Minutes.\n Confirmation Link: '+str(link)
            mail.send(email,msg)
            session['email']=request.form['email']
            api.user_signup(form_details['name'],form_details['email'],form_details['pass'],"1")
            return render_template('index.html')
        else: return render_template('login.html')    
    return render_template('signup.html')    



@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        form_details = request.form
        if api.mail_confirm(form_details['email'])==True:
            data=api.login(form_details['email'],form_details['pass'])
            if(data=='correct_password'):
                session['email']=form_details['email']
                return render_template('index.html')
            elif data=='wrong_password':
                return render_template('login.html')
            elif data == 'username_dosenot_exist':
                return  render_template('login.html')
        return  render_template('login.html')   
    return render_template('login.html')


@app.route('/logout',methods=['POST','GET'])
def logout():
    session.pop('email',None)
    return render_template('login.html')

@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email=s.loads(token,salt='email-confirm',max_age=600)
        api.update(email)
        return render_template('untitled.html')
    except SignatureExpired:
        email=s.loads(token,salt='email-confirm')
        api.delete(email)
        return '<h1>Token expired</h1>'   


if __name__=='__main__':
    app.run(debug=True)