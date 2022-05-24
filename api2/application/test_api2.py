from unittest.mock import patch
from flask import url_for, Flask
from flask_testing import TestCase
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestStrength(TestBase):
    def test_Strength(self):
            response = self.client.get(url_for('post_title'))
            self.assertIs(response.data != None, True)