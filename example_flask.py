from flask import render_template #头部，引入模板渲染方法
 
@app.route("/login",methods=["GET"])
def login():
 return render_template("/login.html") 