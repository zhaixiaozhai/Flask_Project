from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
import config

#Flask-SQLALchemy的使用
# 1.初始化和设置数据库的配置信息
#     *使用"flask-sqlalchemy"中的SQLALchemy进行初始化
# 3.在主app中添加配置文件

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
# 4.做测试，看有没有问题
db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)


# 2.设置配置信息：
#     *在config文件中添加以下信息
#     *dialect+driver://username:password@host;port/database
'''
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD= 123456
HOST='127.0.0.1'
PROT='3306'
DATABASE='db_demo1'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PROT,DATABASE)
'''