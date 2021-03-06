# project/tests/test_user_model.py

import unittest

from project.server import db
from project.server.models import User
from project.tests.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_encode_access_token(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_access_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

if __name__ == '__main__':
    unittest.main()