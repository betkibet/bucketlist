import unittest
import app
from app.tests import UserInfo, Account
from app.views import create, view
class BucketTest(unittest.TestCase):
    def setUp(self):
        self.bucket_info = ["index", "activity", "date"]
    def test_redirect_homepage(self):
        '''' .....Test for Homepage Redirect.....'''
        path = app.app.test_client()
        path.get('/')
        self.assertNotEqual('welcome to bucketlist', None)
    def test_redirect_register(self):
        '''' .....Test for Reigstration Redirect.....'''
        path = app.app.test_client()
        path.get('/register')
        self.assertNotEqual('/register_submit', None)
    def test_redirect_bucketlist(self):
        '''' .....Test for Create_Bucketlist Redirect.....'''
        path = app.app.test_client()
        path.post('/create')
        self.assertNotEqual(create, None)
    def test_redirect_view_bucketlist(self):
        '''' .....Test for View bucketlist Redirect.....'''
        path = app.app.test_client()
        path.post('/view')
        self.assertNotEqual(view, None)
    def test_create_bucket_info(self):
        '''' .....Test for Bucket Create .....'''
        self.assertNotEqual(self.bucket_info.index, None)
    def test_create_bucket_if_not_authenticated(self):
        '''' .....Test for Bucket Create When user is not logged in.....'''
        self.user_info = False
        self.assertEqual(self.user_info, Account(True)), "You must be logged in to create a bucket"
    def test_user_authentication(self):
        '''' .....Test for User Authentication.....'''
        self.user_info = "user", "pass"
        self.assertEqual(self.user_info, UserInfo("userx", "pass")), "Credentials are incorrect"

def main():
    unittest.main()
