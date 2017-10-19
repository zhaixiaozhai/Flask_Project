# 本程序无法运行 介绍一种思想
# 把模型单独放在一个文件中
# 如何解决循环引用，把'db'放在一个单独的文件中，请切断循环引用的线条就可以了
##################循环引用######################
from flask import Flask
# from  flask_sqlalchemy import SQLAlchemy
from  models import Artcile
from exts import db
app = Flask(__name__)
# db=SQLAlchemy(app)
db.init_app()

db.create_all()

# class Artcile(db.Model):
#     __tablename__ = 'article'
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     title = db.Column(db.String(100),nullable=False)
# db.create_all()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
