from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newflask.db'
db = SQLAlchemy(app)


class PostModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    text = db.Column(db.Text, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/post')
def post_list():
    posts = PostModel.query.all()
    return render_template('post_list.html', posts=posts)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        post = PostModel(title=title, text=text)

        try:
            db.session.add(post)  # добавляем в БД запись
            db.session.commit()  # сохраняем запись
            return redirect('/')
        except:
            return f'Произошла ошибка :('

    else:
        return render_template('create.html')



if __name__ == '__main__':
    app.run(debug=True)