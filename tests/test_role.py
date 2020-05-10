from app.models import User,Role
from app import db
import unittest


class RoleModelTest(unittest.TestCase):
    def setUp(self):
        self.new_role = Role( id = 3, name = "Admin" )

    def tearDown(self):
        User.query.delete()
        Role.query.delete()

    def test_check_instance(self):
        self.assertEqual(self.new_role.id, 3)
        self.assertEqual(self.new_role.name, "Admin")
