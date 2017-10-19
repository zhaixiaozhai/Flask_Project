#####使用Flask-SQLAlchemy创建模型与表的映射：
# 1.模型需要集成子'db.Modle'然后必须映射到表中属性，必须携程'db.Column()'的数据类型
    # *db.Integer代表整型
    # *db.String代表varchar
    # *db.text代表的是text
# 其他参数：
# ’primary_key':代表将这个字段上设置为主键
# 'autoincrement'代表的是这个 主键为自增长的
# 'nullable'代表中的是这个字段是否为空，默认为空
# 最后西药调用'db.create_all'来讲模型真正的创建到数据库中
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer,primary_key =True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text(100),nullable=False)
db.create_all()

@app.route('/')
def hello_world():
    article1 = Article.query.filter(Article.content == 'bbb').first()
    db.session.delete(article1)
    db.session.commit()
    return 'Hello World!'
    # article1 = Article(title='aaa',content='bbb')
    # db.session.add(article1)
    # # 事务的操作-提交
    # db.session.commit()

    # # 查数据
    # # select * from article where title='aaa';
    # result = Article.query.filter(Article.title == 'aaa').all()
    # print(result[0].title)


    # # 改：
    # # 1.先把你要更改的数据查出来
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # # 2.把这条数据需要修改的地方进行修改
    # article1.title = 'new title'
    # # 3.做事务的提交
    # db.session.commit()
    # return 'Hello World!'

    # # 删除
    # # 1.把需要删除的数据查找出来
    # article1 = Article.query.filter(Article.content == 'bbb').first()
    # # 2.把这条数据删除掉
    # db.sessiond.delete(article1)
    # # 3.做事务提交
    # db.session.commit()
    #
    #
    # return  'Hellp World!'

if __name__ == '__main__':
    app.run()
