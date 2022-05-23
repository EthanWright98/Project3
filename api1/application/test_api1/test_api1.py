from unittest.mock import patch
from flask import url_for, Flask
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestWeapon(TestBase):
    def test_Claymore(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for(get_weapon))
            self.assertIn(b'Claymore', response.data)


    def test_Fists(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for(get_weapon))
            self.assertIn(b'Fists', response.data)


    def test_Spear(self):
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for(get_weapon))
            self.assertIn(b'Spear', response.data)

    def test_Flail(self):
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for(get_weapon))
            self.assertIn(b'Flail', response.data)


    def test_Bow(self):
        with patch('random.randint') as r:
            r.return_value = 4
            response = self.client.get(url_for(get_weapon))
            self.assertIn(b'Bow', response.data)