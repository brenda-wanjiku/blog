from ..models import User,Role,Blog,Comment,Quote
from .. import db
from . import main
from flask import render_template, redirect, url_for,flash
from ..requests import get_quotes
from flask_login import login_required, current_user

@main.route('/')
def index():
    title = "HOMEPAGE"
    blog = Blog.display_blogs()
    quotes = get_quotes()
    return render_template('index.html', title = title, blog = blog, quotes = quotes )

@main.route('/blog/<blog_id>')
def blog(blog_id):
    title = "Blogs"
    blogs = Blog.query.filter_by(id = blog_id).all()
    return render_template('blog.html', title = title,blogs = blogs)