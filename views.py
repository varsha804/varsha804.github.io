from flask import render_template, Flask
from project import app, pages
# from app import app

@app.route('/')
def home():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('templates/home.html', pages=sorted_posts)
