# from flask import Flask, request, render_template
 
# app = Flask(__name__)

# @app.route("/login",methods=["GET"])
# def login():
#  return render_template("/login.html") 

# @app.route('/')
# def index():
#      return render_template('login.html')


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)  