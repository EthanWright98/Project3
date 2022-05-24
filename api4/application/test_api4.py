from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_console(self):
        with patch("requests.get") as g:
            with patch("requests.post") as p:
                g.return_value.text = "Bow 1"
                response = self.client.get(url_for('get_gladiator'), data = p)
                print(response.data)
                self.assertIn(b'Gladiator generator', response.data)