from ..models import User,Role,Blog,Comment
from .. import db
from . import main
from flask import render_template


@main.route('/')
def index():
    title = "HOMEPAGE"
    return render_template('index.html')

@main.route('/blog/<blog_id>')
def blog(blog_id):
    title = "Blogs"
    blogs = Blog.get_blog(id = blog_id).all()
    return render_template('blog.html', blogs = blogs)