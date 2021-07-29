import unittest
from unittest.mock import patch

from app import create_app
from app.people_service import PeopleService


class TestPeopleRoutes(unittest.TestCase):

    def setUp(self) -> None:
        self.app = create_app('testing')
        self.test_client = self.app.test_client()

    def test_retrieve_people_calls_people_service_with_None_when_sort_arg_missing(self):
        with patch.object(PeopleService, 'retrieve_all') as mock_retrieve_all:
            self.test_client.get('/people')
            mock_retrieve_all.assert_called_with(None)

    def test_retrieve_people_calls_people_service_with_sort_arg_when_passed(self):
        with patch.object(PeopleService, 'retrieve_all') as mock_retrieve_all:
            self.test_client.get('/people?sort=name')
            mock_retrieve_all.assert_called_with('name')

    def test_retrieve_people_calls_people_service_with_descending_sort_arg_when_passed(self):
        with patch.object(PeopleService, 'retrieve_all') as mock_retrieve_all:
            self.test_client.get('/people?sort=-name')
            mock_retrieve_all.assert_called_with('-name')

    def test_retrieve_people_returns_results(self):
        with patch.object(PeopleService, 'retrieve_all') as mock_retrieve_all:
            mock_retrieve_all.return_value = [{'key1': 'value1'}, {'key2': 'value2'}]

            rv = self.test_client.get('/people?sort=-name')
            result = rv.json

            self.assertEqual(result, [{'key1': 'value1'}, {'key2': 'value2'}])
            self.assertEqual(rv.status_code, 200)


