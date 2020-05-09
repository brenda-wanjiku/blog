from ..models import User,Role,Blog,Comment
from .. import db


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/blog/<blog_id>')
def blog(blog_id):
    title = "Blogs"
    blogs = Blog.get_blog(blog_id = blog_id).all()
    return render_template('blog.html', blogs = blogs)