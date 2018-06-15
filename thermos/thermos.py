from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
from forms import BookmarkForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'oy\xe6W\xe1\xddJ\xaa\x1f-$\xb6\xe0\x95d\xf3^\xc1\x10<]\xf4U\xf2'
bookmarks = []

class User:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def initials(self):
        return self.firstName + " " + self.lastName

    def __str__(self):
        return self.firstName + " " + self.lastName

def store_bookmark(url, description):
    bookmarks.append(dict(
        url = url,
        user = "My Name",
        description = description,
        date = datetime.utcnow()
    ))

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]

# Basic View
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks = new_bookmarks(5))

# Bookmarks View
@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
        flash("Stored bookmark '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form = form)

# 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# 500 error page
@app.errorhandler(500)
def server_error(e):
    return render_template('500.hmtl'), 500

if __name__ == '__main__':
    app.run(debug=True)