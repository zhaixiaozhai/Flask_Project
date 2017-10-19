# flask-maigrate
# 1.介绍：因为采用'db。create_all'在后期修改字段的时候，不会自动映射到数据库中，不会自动的映射到数据库中，
#        必须删除表重新运行'db.create_all'才会重新映射，这样不符合我们的需求。
#        因此flask_migrate就是为了解决这个问题，他可以在每次修改模型后，可以将修改的东西映射到数据库中。
# 2.安装'pip install flask-migrate

from flask import Flask
from exts import db
import config
from models import Article

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
with app.app_context():
    db.create_all()
# 上下文#################################


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
