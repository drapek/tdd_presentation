import unittest
from example_crashed_py_file.app import app


class MainAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_invoices(self):
        resp = self.app.get('/invoices/')
        self.assertEqual(resp.status_code, 200)
