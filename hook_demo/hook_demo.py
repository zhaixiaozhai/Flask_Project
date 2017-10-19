from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import redirect
import os

app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)

# before_request: 在请求之前执行
# before_request是在视图函数执行之前执行的
# before_request这个函数只是一个装饰器，可以把需要设置为钩子函数的代码放到视图函数执行之前来执行
@app.before_request
def my_before_request():
    # if session.get('username'):
    #     g.username = session.get('username')
    print('hello')

# context_pro
@app.route('/login/',methods=['GET','POST'])
def login():
    print('login')
    if request.method=='GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username=='root'and password=='123456':
            session['username']='root'
            return u'登陆成功'
        else:
            return u'用户名或者密码错误'
@app.route('/edit/')
def edit():
    if session.get('username'):
        return u'修改成功';
    # if hasattr(g,'username'):
    #     return u'修改成功'
    else:
        return redirect(url_for('login'))
@app.route('/')
def hello_world():
    print('index')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
