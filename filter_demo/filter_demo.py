# 过滤器的介绍：
# *介绍：过滤器可以处理变量把原始的变量经过处理后在展示出来,作用的对象是变量
# *语法：
#     """
#     {{avatar|default('xxx')}}
#     """
# default过滤器，如果当前变量不存在，这时候可以指定默认值
# length过滤器：求列表或者字符串或者字典或者元组的长度。
# 常用过滤器等等
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    user_comments = [
        {
            'user':u'sunhaiyang',
            'content':'very nice'
        },
        {
            'user':u'孙海洋',
            'content':'非常不错'
        }
    ]
    return render_template("index.html",comments=user_comments)
# avatar = "https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png")


if __name__ == '__main__':
    app.run(debug=True)
