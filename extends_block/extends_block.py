# 继承的作用和语法
#  *作用：可以吧一些公共的代码放在父模板中，避免每个模板写同样的代码
#  *语法{{extends 'xxx.html'}}
#  block作用:可以让子模板实现自己的需求，父模板需要提前定义好
from flask import Flask
from flask import render_template

app = Flask(__name__)

#  python的类继承
# class Person(object):
#     name = 'xxxx'
#     age = '12'
#
# class Student(Person):
#     pass

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
