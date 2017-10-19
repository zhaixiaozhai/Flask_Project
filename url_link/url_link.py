# url链接：使用'url_for(视图函数名称)'可以反转成url
# 加载静态文件
# 语法'{{ url_for('static',filename='路径') }}'
# 静态文件，flask会从'static'文件夹中开始寻找，所以不需要在写'static'这个路径了
# 可以加载'css'文件，可以加载'js'文件，还有'image'文件
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
