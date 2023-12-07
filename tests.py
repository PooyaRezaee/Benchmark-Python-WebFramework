import requests
import unittest

class FastApiTest(unittest.TestCase):
    def test_fast_api_up(self):
        response = requests.get('http://127.0.0.1:7000/')
        self.assertEqual(response.status_code,200)

class DjangoTest(unittest.TestCase):
    def test_django_up(self):
        response = requests.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code,200)

class FlaskTest(unittest.TestCase):
    def test_flask_up(self):
        response = requests.get('http://127.0.0.1:5000/')
        self.assertEqual(response.status_code,200)


if __name__ == '__main__':
    unittest.main()