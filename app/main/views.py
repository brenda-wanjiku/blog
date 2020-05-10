from ..models import User,Role,Blog,Comment,Quote
from .forms import AddBlog
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


@main.route('/blog/<blog_id>/new', methods = ['GET', 'POST'])
@login_required
def add_blog(blog_id):
    title = "Add comment"
    form = AddBlog()
    new_blog = None

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data

        new_blog = Blog( title = title, description = description)
        new_blog.save_blog()

        title = "New Blog"
        blogs = Blog.query.all()
        return redirect(url_for('main.blog', title = title, blogs = blogs, id  = blog_id))
    return render_template('new_blog.html', form = form, title =title)





     