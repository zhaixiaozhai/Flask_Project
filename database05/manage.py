#encoding: utf-8
# 可以通过命令行的形式来操作Flask，例如通过跑一个开发版本的服务器，设置数据库，定时任务等。
# 安装"pip install flask-script"
# 如果直接在住'manage.py'中写命令，那么终端只需要'python manage.py command_name'就可以了
# 如果把一些命令集中在一个文件中，那么早终端就需要输入一个父命令，比如'python manage.py db intit'
# db_scripts是子命令
from flask_script import Manager
from database05 import app
from db_scripts import DBmanager

manager = Manager(app)

# 和数据库相关的操作都放在一起
manager.add_command('db',DBmanager)


@manager.command
def runserver():
    print("服务器跑起来了")

if __name__=='__main__':
    manager.run()