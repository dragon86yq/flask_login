from flask import Flask, request, render_template, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'  

@app.route('/', methods=["GET"])
def base():
  return render_template("base_index.html") 

@app.route('/login', methods=["GET"])
def login():
  return render_template("login.html") 

@app.route('/login_user', methods=["GET", "POST"])
def loginpost():
    username = request.args.get('username')
    password = request.args.get('password')
    # username = request.form.get("username")
    # password = request.form.get("password")
    if username == "test" and password == "123":
        return render_template("register.html")
    else:
        return render_template("base_index.html") 

@app.route("/register", methods = ["GET" or "POST"])
def registerPost():
    # username  = request.form.get("username","")
    # password  = request.form.get("password", "")
    # repassword = request.form.get("repassword", "")
    username  = request.args.get("username")
    password  = request.args.get("password")
    repassword = request.args.get("repassword")
    email          = request.form.get("email")
    if len(username) == 0:
        flash("username is blank")
        return render_template("base.html")
    elif len(password) == 0:
        flash("password is blank")
        return render_template("base.html")    
    elif len(email) == 0:
        flash("email is blank")
        return render_template("base.html")
    else:
        return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True)  