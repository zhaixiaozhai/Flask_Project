# DEBUG = True
# 新建一个config.py文件
# 在主app文件导入这个文件，并且配置到‘app'中，示例代码如下
# app.config.from_object(config)
# 其他参数，后期都是放在这个配置文件中
import  os

# SECRET_KEY
# SQLALCHEMY等配置文件
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo2'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# SQLALCHEMY_DATABASE_URI = True

SQLALCHEMY_TRACK_MODIFICATIONS = True
#=
# SECRET_KEY = os.urandom(24)