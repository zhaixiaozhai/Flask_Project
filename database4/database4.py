#encoding utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

# 用户表
# Create table users（
#     IDintprimary key autoincrement,
#     username varchar(100) not null
# )
# 文章表 外键
# Create table users（
#     idintprimary key autoincrement,
#     title varchar(100) not null
#     content text not null
#     author_id int,
#     foregin key 'author id' references'users.id'
# )
################外键##########################
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    # password = db.Column(db.String(100),nullable=False)
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    author = db.relationship('User',backref=db.backref('articles'))
    #给'Article'这个模型添加一个'author'属性可以访问这篇文章的作者的数据，想访问普通模型一样
    #backref定义反向引用，可以通过User.articles这个模型访问这个作者缩写的所有文章
db.create_all()

# 想要添加一篇文章，因为文章必须依赖用户存在，所以先添加一个用户
#
# user1=User(username = 'sunhaiyang')
# db.session.add(user1)
# db.session.commit()
#
# article1 = Article(title='aaa',content='bbbb',author_id=1)
# db.session.add(article1)
# db.session.commit()

@app.route('/')
def hello_world():
    # # 我要找标题为aaa的作者
    # article = Article.query.filter(Article.title == 'aaa').first()
    # author_id = article.author_id
    # user = User.query.filter(User.id==author_id).first()
    # print( user.username)

    # article = Article(title='aaa',content='bbb')
    # article.author = User.query.filter(User.id==1).first()
    # db.session.add(article)
    # db.session.commit()
    # author = User.query.filter(User.username=='sunhaiyang').first()

    # 我要找到作者写过的所有文章
    user =User.query.filter(User.username=='sunhaiyang').first()
    result = user.articles
    for i in result:
        print('-'*10)
        print(i.title)
    return 'Hello World!'



if __name__ == '__main__':
    app.run(debug=True)


