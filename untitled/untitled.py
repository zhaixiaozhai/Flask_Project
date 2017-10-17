# 从flask框架中导入flask这个类
from flask import Flask,redirect,url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import config
# import _mysql
# 初始化一个Flask对象 app
# 需要出第一个参数__name__
# 1.方便flask框架寻找资源
# 2.方便flask插件比如flask——sqlalchemy出现错误的时候，去寻找问题所在位置
app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

# 创建article表:
# create table article{
#     id int primary key autoincrement,
#     title varchar(100)not null,
#     content text  not null,
# }

class Article(db.Model):
    __tablename__='article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)

db.create_all()

@app.route('/')
def database():
    return 'Hello'

###模板渲染和参数
# 1.如何渲染模板
#   *模板放在文件夹下
#   *在flask导入render_template函数
#   *在视图函数中，使用'render_template'函数，渲染模板、注意：模板只需要填写模板的名字，不需要填写'template'文件夹的路径
# 2.模板传参：
#   *如果只有一个或者少量参数，直接在'render_template'函数中添加关键字参数就可以了
#   *如果有多个参数的时候，那么可以先把所有的参数放在字典中，然后在'render_template'中使用两个**把字典转换成关键参数传递进去，这样代码更方便管理和使用
# 3.在模板中，如果使用一个变量，语法是{{ params}}
# 4.访问木星中的属性或者字典可以通过{{params.property}}的形式，或者通过{{params['age']}}
# @app.route('/')
# def start():
#     class Person(object):
#         name = u'孙海洋'
#         age = 22
#     p = Person()
#     context={
#         'username':u'admin',
#         'gender':u'男',
#         'age':18,
#         'person':p,
#         'websites':{
#             'baidu':'www.baidu.com',
#             'google':'www.google.com'
#         }
#     }
#     return render_template('template01.html',**context)

# if判断语句
# 1.语法
# '''
#     {% if xxx %}
#     {% else %}
#     {% endif %}
# '''
# 2.if的使用，和python相差无几
# @app.route('/<is_login>/')
# def index(is_login):
#     if is_login=='1':
#         user_context={
#             'username':u'孙海洋',
#             'age':19
#         }
#         return render_template('template02.html',user=user_context)
#     else:
#         return render_template('template02.html')


# for遍历字典
# 1.字典的遍历，语法和python一样，可以使用items(),keys(),values(),iteritems(),iterkeys(),itervalues()
# 2.列表的遍历，语法和python一样
# @app.route('/forindex/')
# def for_index():
#     # usr_dict={
#     #     'username':u'孙海洋',
#     #     'age':19
#     # }
#     # websites_list=['baidu.com','google.com']
#     # for k,v in usr_dict.items():
#     #     print(k)
#     #     print(v)
#     # return render_template('template03.html',user=usr_dict,websites=websites_list)
#
#     books=[
#         {
#             'name':u'西游记',
#             'author':u'吴承恩',
#             'price':109
#         },
#         {
#             'name': u'红楼梦',
#             'author': u'曹雪芹',
#             'price': 200
#         },
#         {
#             'name': u'三国演义',
#             'author': u'罗贯中',
#             'price': 129
#         },
#         {
#             'name': u'水浒传',
#             'author': u'施耐庵',
#             'price': 159
#         }
#     ]
#     return  render_template('template03.html',lalal=books)
#
# @app.route('/default')
# def default():
#     return render_template('template04.html')
###跳转和重定向
# 导入两个函数redirect,url_for
#   *redirect()：重定向
#   *url_for：URL反转
# 在用户访问一些需要登录的页面的时候，如果用户没有登录，那么可以重定向到登录界面
# 代码实现：
# @app.route('/')
# def hello():
#     # rediect传一个URL,重定向到login页面
#     # return redirect('/login/')
#     login_url=url_for('login')
#     return redirect(login_url)
#     return u"这是首页"
#
# @app.route('/login/')
# def login():
#     return u"这是登录界面"
#
# @app.route('/question/<is_loading>/')
# def question(is_loading):
#     if is_loading==1:
#         return u"这是发布问答的界面"
#     else:
#         return redirect(url_for('login'))

# app.route是一个装饰器
# @开头在函数上面
# 这个装饰器的作用是url与视图函数的映射
# 127.0.0.1：:5000/ ->请求函数，然后返回给浏览器
# @app.route('/index')
# @app.route('/index')
# def index():
#     return render_template("Login.html")

### url传参
# 1.参数的作用，可以在相同的URL，但是指定不同的参数，来加载不同的数据
# 2.在flask如何使用参数，代码：
# 参数需要放在两个尖括号中如<id>
# 视图函数中需要放和URL中参数同名的参数
# @app.route('/article/<id>')
# def article(id):
#     return '您请求的参数是：%s'%id

### URL反转
# 1.从视图函数到URL的转换
# 2.反转URL的用处
#       *在页面重定向的时候使用URL反转
#       *在模板中也会使用
# @app.route('/list/')
# def my_list():
#     return 'list'



if __name__ == '__main__':
    # 如果当前这个文件时作为入口程序运行，那么就执行app.run
    # 启动一个应用服务器，来接受用户的请求
    # while True
    # listen()
    # debug=True就设置当前项目为debug，
    # debug模式两大功能：
    # 1.当程序出现问题的时候，可以在页面中看到错误信息和出错的位置。
    # 2.只要修改了项目中的python文件，文件会自动加载，不需要重新启动服务器
    app.run(debug=True)
