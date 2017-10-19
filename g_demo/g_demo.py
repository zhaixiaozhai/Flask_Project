# g属性
# 1.g对象是专门用来保存用户的数据的
# 2.g对象再一次请求中所有的代码都是可以使用的
from flask import Flask,request,render_template
from flask import g
from utils import login_log

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('index.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username=='sunhaiyang' and password =='111111':
            #g对象用来绑定用户，在所有页面都可以使用
            # login_log(username)
            g.username = 'sunhaiyang'
            login_log()
            return u'登陆成功'
        else:
            return u'您的用户名或密码错误'
if __name__ == '__main__':
    app.run(debug=True)
