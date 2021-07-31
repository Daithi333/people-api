import unittest

from app import create_app


class TestIndexRoutes(unittest.TestCase):

    def setUp(self) -> None:
        self.app = create_app('testing')
        self.test_client = self.app.test_client()

    def test_index_route_returns_response(self):
        rv = self.test_client.get('/')
        result = rv.json

        self.assertEqual(result, {'status': 'ok'})
        self.assertEqual(rv.status_code, 200)

    def test_invalid_route_returns_404_status(self):
        rv = self.test_client.get('/invalid')
        result = rv.json

        self.assertEqual(result, {'message': 'Requested route not found on server'})
        self.assertEqual(rv.status_code, 404)

    def test_invalid_method_returns_405_status(self):
        rv = self.test_client.put('/')
        result = rv.json

        self.assertEqual(result, {'message': 'Invalid method on request'})
        self.assertEqual(rv.status_code, 405)
