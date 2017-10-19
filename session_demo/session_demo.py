from flask import Flask
# session的操作方式：
#   *使用'session'需要从'flask'中导入，以后所有和'session'相关的操作都是通过这个变量来的
#   *使用'session'需要设置'SECRET_KRY'，用来作为加密用的，并且这个'SECRET_KRY'如果每次服务器启动后都变化的话，
#       那么之前的'session'就不能在通过当前这个'SECRET_KRY'进行解密了
#   *操作'session'的时候和操作的字典是一样的
from flask import session
import config
from datetime import timedelta

app = Flask(__name__)
app.config.from_object(config)
# 可以通过如下更改设置过期时间，这个值得数据类型是'datatime.timedelay'类型
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7)
# 添加数据到session中
# 操作session跟操作字典是一样的
# SECRET_KEY
@app.route('/')
def hello_world():
    session['username']='sunhaiyang'
    # 如果没有指定session的过期时间，那么默认是浏览器关闭就会自动消失
    # 如果设置了session的permanent的属性为True 那么过期时间为31天
    session.permanent = True
    return 'Hello World!'
#获取
@app.route('/get/')
def get():
# session['username']
# session.get('username')
    return session.get('username')

@app.route('/delete/')
def delete():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))
    return 'successful'
#删除session中的所有数据
@app.route('/clear/')
def clear():
    print(session.get('username'))
    session.clear()
    print(session.get('username'))
    return 'successful'

if __name__ == '__main__':
    app.run(debug=True)
