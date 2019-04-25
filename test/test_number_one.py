import unittest
from biger_blog import create_app
from biger_blog.extends import db

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app("test")
        db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()