# coding=utf-8
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mako import MakoTemplates, render_template

app = Flask(__name__)
mako = MakoTemplates(app)
app.config['SECRET_KEY'] = '123456'  # a random string
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1:3306/net_news_v3_db?charset=utf8'
db = SQLAlchemy(app)


class News(db.Model):
    """ news model """
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    content = db.Column(db.String(300), nullable=False)
    is_valid = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<News {}>'.format(self.title)


@app.route('/')
def index():
    """ news index page """
    news_list = News.query.all()
    return render_template('index.html', news_list=news_list)


@app.route('/cat/<name>/')
def cat(name):
    """ news category page """
    news_list = News.query.filter_by(is_valid=1, type=name)
    return render_template('cat.html', name=name, news_list=news_list)


@app.route('/detail/<int:pk>/')
def detail(pk):
    """ news detail page """
    new_obj = News.query.get(pk)
    return render_template('detail.html', new_obj=new_obj)


if __name__ == '__main__':
    app.run(debug=True)
