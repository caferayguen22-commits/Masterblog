import json
from flask import Flask, render_template

app = Flask(__name__)


def load_posts():
    """Hilfsfunktion: Lädt die Beiträge live aus der JSON-Datei."""
    with open("blog_posts.json", "r", encoding="utf-8") as file:
        return json.load(file)


@app.route('/')
def index():
    # 1. Daten aus der JSON-Datei holen
    blog_posts = load_posts()
    # 2. Die Liste an die index.html übergeben
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)