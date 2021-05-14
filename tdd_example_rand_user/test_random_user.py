import unittest
import random

from tdd_example_rand_user.app import app


class RandomUserTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_happy_path(self):
        resp = self.client.get('/random_user')
        self.assertEqual(resp.status_code, 200)

    def test_random_user_shown(self):
        resp = self.client.get('/random_user')
        self.assertTrue(resp.data.decode('utf-8') != '')

    def test_get_full_user_data(self):
        random.seed(534)
        resp = self.client.get('/random_user')
        self.assertEqual(resp.data.decode('utf-8'), 'Krzysztof Krawczyk')

    def test_get_another_user(self):
        random.seed(500)
        resp = self.client.get('/random_user')
        self.assertEqual(resp.data.decode('utf-8'), 'Otylia Jędrzejczak')
