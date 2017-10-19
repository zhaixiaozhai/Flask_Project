from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
# get请求是通过'flask.request.args'来获取
# post请求是通过'flask.request.forms'来获取
# post请求在模板中要注意几点：
# input标签中，要写name来标识这个value的key，方便后台获取
# 在写form表单的时候，要制定'method=post'，并且要指定'action='/login/''
@app.route('/search/')
def search():
    q =request.args.get('q')
    return "用户提交的查询参数是 %s"%q
# 默认的视图函数只能采用get请求
# 如果想采用post请求，要写明
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print(username,password)
        return "post请求"
if __name__ == '__main__':
    app.run(debug=True)
