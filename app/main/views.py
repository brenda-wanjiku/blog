from ..models import User,Role,Blog,Comment
from .. import db
from . import main
from flask import render_template


@main.route('/')
def index():
    title = "HOMEPAGE"
    blog1 = Blog.get_blog('1')
    return render_template('index.html', title = title, blog1 = blog1 )

@main.route('/blog/<blog_id>')
def blog(blog_id):
    title = "Blogs"
    blogs = Blog.query.filter_by(id = blog_id).all()
    return render_template('blog.html', title = title,blogs = blogs)