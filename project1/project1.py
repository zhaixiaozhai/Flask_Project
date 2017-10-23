from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import config
from exts import db
from models import User

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        userphone=request.form.get('telephone')
        password=request.form.get('password')

        user = User.query.filter(User.telephone==userphone,User.password==password).first()

        if user:
            session['user_id']=user.id
            # 如果想在31天不需要登录
            # session.per,anent = True
            return redirect(url_for('index'))
        else:
            return u'账号或者密码错误'


@app.route('/regist', methods=['GET', 'POST'])
def regist():
    if request.method=='GET':
        print('a')
        return render_template('regist.html')
    else:
        telephone = request.form.get('phonenumber')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # 手机号码如果被注册就不能在注册了
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            print('该手机号已经注册')
            return u'该手机号已经注册'
        else:
            if password1 != password2:
                return u'请确认密码'
            else:
                print('未被注册')
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))

@app.route('/loginout/')
def logout():
    session.clear()
    return redirect(url_for('login'))



@app.route('/question/',methods=['GET','POST'])
def question():
    if request.method=='GET':
        return render_template('question.html')
    else:
        pass
# 上下文处理器应该返回一个字典，字典中的'key'会被模板中当成变量来渲染
# 上下文处理器中返回的字典，在所有页面中都是可用的
# 被这个装饰器修饰的钩子函数，即使为空必须要返回一个字典
@app.context_processor
def contenxt_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user':user}
    return {}





if __name__ == '__main__':
    app.run()
