from flask_news import db, News


def UrlToText(content):
    prefix = "C:/Users/ChienI/Desktop/flask_news/flask_news_v3"

    # new_content: absolute path
    # content: relative path
    new_content = prefix + content
    with open(new_content, "r", encoding="utf-8") as f:
        data = f.read()
    return data


# test add a new news to News
news1 = News(
    title="马云向美国捐100万只口罩和试剂盒 网友：为中国争脸？",
    type="科技",
    image="/static/img/news/news_6/news6.png/",
    content="/static/img/news/news_6/news6.txt"
)

db.session.add(news1)
db.session.commit()
