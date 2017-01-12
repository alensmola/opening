import unittest, os, tempfile
from pprint import pprint
from json import loads
import api


class ApiTest(unittest.TestCase):
    def setUp(self):
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()
        with api.app.app_context():
            pass
            # api.init_db()

    def get_json(self, path):
        response = self.app.get(path)
        return loads(response.get_data(as_text=True), 'utf8')

    def test_index(self):
        self.assertEqual(self.get_json('/')['status'], 'ok')


if __name__ == '__main__':
    unittest.main()
