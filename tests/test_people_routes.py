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

    def test_add_person_calls_people_service_add_one_with_json_data(self):
        with patch.object(PeopleService, 'add_one') as mock_add_one:
            mock_add_one.return_value = {'id': '1', 'key1': 'value1', 'key2': 'value2'}

            self.test_client.post('/people', json={'key1': 'value1', 'key2': 'value2'})

            mock_add_one.assert_called_with({'key1': 'value1', 'key2': 'value2'})

    def test_add_person_returns_results_including_id(self):
        with patch.object(PeopleService, 'add_one') as mock_add_one:
            mock_add_one.return_value = {'id': '1', 'key1': 'value1', 'key2': 'value2'}

            rv = self.test_client.post('/people', json={'key1': 'value1', 'key2': 'value2'})
            result = rv.json

            self.assertEqual(result, {'id': '1', 'key1': 'value1', 'key2': 'value2'})
            self.assertEqual(rv.status_code, 201)

    def test_update_person_calls_people_service_update_one_with_id_and_json_data(self):
        with patch.object(PeopleService, 'update_one') as mock_update_one:
            mock_update_one.return_value = {'id': '1', 'key1': 'value1', 'key2': 'value2'}

            self.test_client.patch('/people/1', json={'key1': 'value1', 'key2': 'value2'})

            mock_update_one.assert_called_with('1', {'key1': 'value1', 'key2': 'value2'})

    def test_update_person_returns_results_including_id(self):
        with patch.object(PeopleService, 'update_one') as mock_update_one:
            mock_update_one.return_value = {'id': '1', 'key1': 'value1', 'key2': 'value2'}

            rv = self.test_client.patch('/people/1', json={'key1': 'value1', 'key2': 'value2'})
            result = rv.json

            self.assertEqual(result, {'id': '1', 'key1': 'value1', 'key2': 'value2'})
            self.assertEqual(rv.status_code, 200)

    def test_delete_person_calls_people_service_delete_one_with_id(self):
        with patch.object(PeopleService, 'delete_one') as mock_delete_one:
            mock_delete_one.return_value = 'Person with id 1 successfully deleted'

            self.test_client.delete('/people/1')

            mock_delete_one.assert_called_with('1')

    def test_delete_person_returns_success_response(self):
        with patch.object(PeopleService, 'delete_one') as mock_delete_one:
            mock_delete_one.return_value = 'Person with id 1 successfully deleted'

            rv = self.test_client.delete('/people/1')
            result = rv.json

            self.assertEqual(result, {'message': 'Person with id 1 successfully deleted'})
            self.assertEqual(rv.status_code, 200)
