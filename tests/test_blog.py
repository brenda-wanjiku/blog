import unittest
from app.models import Blog,User,Comment

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username = "Brenda")
        self.new_blog = Blog(title = "blog", user = self.new_user)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
        Comment.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))

    def test_init(self):

        self.assertEquals(self.new_blog.title, "blog")

    def test_save_blog(self):
        self.new_blog.save_blog()
        blogs = Blog.query.all()
        self.assertTrue(len(blogs) > 0)

    def test_relationship_user(self):
        user = self.new_pitch.blog.username
        self.assertTrue(user == "Brenda")