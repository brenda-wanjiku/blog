import unittest
from app import db
from app.models import Comment, User


class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_bre = User(username = 'Brenda',password = 'bread', email = 'bre@gmail.com')
        self.new_comment = Comment(blog_id=2,title='comment',comment='test_comment',user = self.user_bre)


    def tearDown(self):
            Comment.query.delete()
            User.query.delete()

    def test_check_instance_variables(self):
            self.assertEquals(self.new_comment.blog_id,2)
            self.assertEquals(self.new_comment.title,'comment')
            self.assertEquals(self.new_comment.comment,'test_comment')
            self.assertEquals(self.new_comment.user,self.user_bre)

    def test_save_comment(self):
            self.new_comment.save_comment()
            self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):
            self.new_comment.save_comment()
            get_comments = comment.get_comments(2)
            self.assertTrue(len(get_comments) == 2)