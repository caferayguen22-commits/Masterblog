import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def load_posts():
    """Hilfsfunktion: Lädt die Beiträge live aus der JSON-Datei."""
    with open("blog_posts.json", "r", encoding="utf-8") as file:
        return json.load(file)

def save_posts(posts):
    with open("blog_posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False, indent=2)


@app.route('/')
def index():
    # 1. Daten aus der JSON-Datei holen
    blog_posts = load_posts()
    # 2. Die Liste an die index.html übergeben
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        blog_posts = load_posts()

        new_id = blog_posts[-1]['id'] + 1 if blog_posts else 1

        new_post = {
            'id': new_id,
            'author': author,
            'title': title,
            'content': content}

        blog_posts.append(new_post)
        save_posts(blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)