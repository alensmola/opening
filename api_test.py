import unittest, os, tempfile
from pprint import pprint
from json import loads, dumps
import requests, responses
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

    def test_list_stations(self):
        stations = self.get_json('/stations')
        self.assertEqual(stations['status'], 'ok')

    def test_list_stations_near(self):
        stations = self.get_json('/stations?near=Ljubljana')
        self.assertEqual(stations['status'], 'ok')

    @responses.activate
    def test_geocode(self):
        responses.add(responses.GET, 'http://maps.googleapis.com/maps/api/geocode/json',
                      dumps({'results': [{'geometry': {'location': {'lat': 1.1, 'lng': 1.1}}}]}))
        result = api.geocode('Fake Lokacija', cache=False)
        self.assertEqual(result, [1.1, 1.1])

    @responses.activate
    def test_geocode_caching(self):
        responses.add(responses.GET, 'http://maps.googleapis.com/maps/api/geocode/json',
                      dumps({'results': [{'geometry': {'location': {'lat': 1.1, 'lng': 1.1}}}]}))
        result = api.geocode('Fake Lokacija')
        self.assertEqual(result, [1.1, 1.1])


if __name__ == '__main__':
    unittest.main()
