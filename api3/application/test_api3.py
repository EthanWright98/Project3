from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_Claymore_pass(self):
        response = self.client.post(url_for('post_chance'), data = 'Claymore 4')
        self.assertIn(b'Thumbs up, you survived', response.data)

    def test_Claymore_perish(self):
        response = self.client.post(url_for('post_chance'), data = 'Claymore 2')
        self.assertIn(b'Thumbs down, you have perished', response.data)

    def test_Fists_pass(self):
        response = self.client.post(url_for('post_chance'), data = 'Fists 10')
        self.assertIn(b'Thumbs up, you survived', response.data)

    def test_Fists_perish(self):
        response = self.client.post(url_for('post_chance'), data = 'Fists 8')
        self.assertIn(b'Thumbs down, you have perished', response.data)

    def test_Spear_pass(self):
        response = self.client.post(url_for('post_chance'), data = 'Spear 4')
        self.assertIn(b'Thumbs up, you survived', response.data)

    def test_Spear_perish(self):
        response = self.client.post(url_for('post_chance'), data = 'Spear 3')
        self.assertIn(b'Thumbs down, you have perished', response.data)

    def test_Flail_pass(self):
        response = self.client.post(url_for('post_chance'), data = 'Flail 7')
        self.assertIn(b'Thumbs up, you survived', response.data)
        
    def test_Flail_perish(self):
        response = self.client.post(url_for('post_chance'), data = 'Flail 5')
        self.assertIn(b'Thumbs down, you have perished', response.data)

    def test_Bow_pass(self):
        response = self.client.post(url_for('post_chance'), data = 'Bow 1')
        self.assertIn(b'Thumbs up, you survived', response.data)

    def test_Bow_perish(self):
        response = self.client.post(url_for('post_chance'), data = 'Bow 0')
        self.assertIn(b'Thumbs down, you have perished', response.data)
    