from flask import Flask, request, render_template, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'  

all_name = []
all_password = []

@app.route('/', methods=["GET"])
def base():
  return render_template("base_index.html") 

@app.route('/login', methods = ["GET"])
def login():
    return render_template("log_in.html")

@app.route('/login_success', methods = ["GET"])
def login_success():
    user_name  = request.args.get("user_name")
    password  = request.args.get("password")
    log_in_sub  = request.args.get("log_in_sub") # value  = 登入
    if log_in_sub == u'登入':
        if len(user_name) == 0 or len(password) == 0:
            return render_template('help.html')
        else:
            if user_name in all_name and password in all_password:
                return render_template("success1.html")
            else:
                return render_template('help.html')
    else:
        return render_template("help.html")


@app.route('/register', methods = ['GET'])
def register():
    return render_template("register.html")

@app.route("/register_success", methods = ["GET" or "POST"])
def registerPost():
    user_name  = request.args.get("user_name")
    password  = request.args.get("password")
    nickname = request.args.get("nickname")
    wechat = request.args.get("wechat")
    location = request.args.get("location")
    agreement = request.args.get("agreement")  # value = agree
    register_sub = request.args.get("register_sub") # value = 提交
    if agreement == 'agree':
        if register_sub == u'提交':
            if len(user_name) == 0 or len(password) == 0:
                return render_template("help.html")
            else:
                all_name.append(user_name)
                all_password.append(password)
                return render_template("log_in.html")
        else:
            return render_template("help.html")
    else:
        return render_template("help.html")



if __name__ == '__main__':
    app.run(debug=True)  