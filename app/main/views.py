from ..models import User,Role,Blog,Comment,Quote
from .forms import AddBlog, SubscriberForm
from .. import db
from . import main
from flask import render_template, redirect, url_for,flash
from ..requests import get_quotes
from flask_login import login_required, current_user

@main.route('/')
def index():
    subscriber_form = SubscriberForm()
    if subscriber_form.validate_on_submit():
        subscriber_email = subscriber_form.email.data
        new_subscriber = Subscriber(email = subscriber_email)
        new_subscriber.save_subscriber()
        mail_message("Welcome to 'Bloggerly'"/"email/welcome_user", new_subscriber.email )
        return render_template(url_for('main.index', id = id))
    title = "Bloggerly"
    blogs = Blog.display_blogs()
    quotes = get_quotes()
    return render_template('index.html',subscriber_form = subscriber_form ,title = title, blogs = blogs,quotes = quotes)


@main.route('/user/<user_id>')
@login_required 
def profile(user_id):
    user = User.query.filter_by(id = user_id).first()
    blogs = Blog.query.filter_by(user_id = user.id).all()
    title = user.username.upper()
    return render_template('profile.html', user= user, blogs = blogs, title= title )

@main.route('/user/<user_id>/update', methods = ["GET", "POST"])
@login_required
def update_profile(user_id):
    title = "Edit Profile"
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        abort(404)
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.profile', user_id = user.id))
    return render_template('update.html', form = form, title = title)



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





     