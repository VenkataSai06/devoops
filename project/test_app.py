import unittest
from project.app import app

class FlaskAppTestCase(unittest.TestCase):

    # Setup test client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test Home Route
    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, this is my first Flask route!")

    # Test About Route
    def test_about_route(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "This is the About page.")

    # Test Invalid Route
    def test_invalid_route(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()