from flask import render_template

from . import main
from ..models import Bookmark, Tag

# Basic View
@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', new_bookmarks = Bookmark.newest(5))

# 401 error page
@main.app_errorhandler(401)
def page_not_authorized(e):
    return render_template('401.html'), 401

# 403 error page
@main.app_errorhandler(403)
def page_not_authorized(e):
    return render_template('403.html'), 403

# 404 error page
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# 500 error page
@main.app_errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@main.app_context_processor
def inject_tags():
    return dict(all_tags=Tag.all)