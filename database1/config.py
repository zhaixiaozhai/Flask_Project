#encoding utf-8


#dialect+driver://username:password@host;port/database
###############################################
#python3驱动使用pymysql
###############################################
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD= 123456
HOST='127.0.0.1'
PROT='3306'
DATABASE='db_demo1'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PROT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False