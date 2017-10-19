from flask import g
def login_log():
    print (u'当前登录用户:%s' % g.username)