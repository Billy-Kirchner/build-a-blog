from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:yes@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(360))
    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/addpost', methods=['POST','GET'])
def addpost():
    if request.method == 'POST':
        title = request.form['new-title']
        body = request.form['new-body']
        new_blog = Blog(title, body)      
        db.session.add(new_blog)
        db.session.commit()
    return render_template('addpost.html')

@app.route("/", methods=['POST','GET'])
def index():
    blogs = Blog.query.all()
    return render_template('blog.html', blogs=blogs)



if __name__ == '__main__':
    app.run()