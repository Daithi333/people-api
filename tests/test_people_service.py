import unittest
from unittest.mock import patch

from app import ResourceNotFoundError
from app.models.person import Person
from app.people_service import PeopleService


class TestPeopleService(unittest.TestCase):
    p1_input_data = {'name': 'Peter', 'age': 33, 'balance': 100.5, 'email': 'test@mail.com', 'address': '12 Road, Belfast'}
    p2_input_data = {'name': 'Rob', 'age': 65, 'balance': 10.55, 'email': 'test2@mail.com', 'address': '12 Street, Belfast'}
    p1 = Person(**p1_input_data)
    p2 = Person(**p2_input_data)
    p1_output_data = {'id': None, **p1_input_data}
    p2_output_data = {'id': None, **p2_input_data}

    @classmethod
    def setUpClass(cls) -> None:
        cls.people_service = PeopleService()

    @patch('app.people_service.Person')
    def test_retrieve_all_calls_Person_query_all(self, person_mock):
        query_all_mock = person_mock.query.all
        query_all_mock.return_value = [self.p1, self.p2]

        self.people_service.retrieve_all(None)

        query_all_mock.assert_called_once()

    @patch('app.people_service.Person')
    def test_retrieve_all_returns_unsorted_results_when_called_with_None(self, person_mock):
        expected = [self.p1_output_data, self.p2_output_data]
        query_all_mock = person_mock.query.all
        query_all_mock.return_value = [self.p1, self.p2]

        result = self.people_service.retrieve_all(None)

        self.assertEqual(result, expected)

    @patch('app.people_service.Person')
    def test_retrieve_all_returns_ascending_sorted_results_when_called_with_sort_key(self, person_mock):
        expected = [self.p1_output_data, self.p2_output_data]
        query_all_mock = person_mock.query.all
        query_all_mock.return_value = [self.p1, self.p2]

        result = self.people_service.retrieve_all('name')

        self.assertEqual(result, expected)

    @patch('app.people_service.Person')
    def test_retrieve_all_returns_descending_sorted_results_when_called_with_sort_key(self, person_mock):
        expected = [self.p2_output_data, self.p1_output_data]
        query_all_mock = person_mock.query.all
        query_all_mock.return_value = [self.p1, self.p2]

        result = self.people_service.retrieve_all('-name')

        self.assertEqual(result, expected)

    @patch('app.people_service.Person')
    @patch('app.people_service.db')
    def test_add_one_calls_Person_query_get(self, db_mock, person_mock):
        session_add_mock = db_mock.session.add
        session_commit_mock = db_mock.session.commit
        query_get_mock = person_mock.query.get
        query_get_mock.return_value = self.p1

        self.people_service.add_one(self.p1_input_data)

        session_add_mock.assert_called_once()
        session_commit_mock.assert_called_once()
        query_get_mock.assert_called_once()

    @patch('app.people_service.Person')
    @patch('app.people_service.db')
    def test_add_one_returns_the_new_person_data(self, db_mock, person_mock):
        query_get_mock = person_mock.query.get
        query_get_mock.return_value = self.p1

        result = self.people_service.add_one(self.p1_input_data)

        self.assertEqual(result, self.p1_output_data)

    @patch('app.people_service.Person')
    @patch('app.people_service.db')
    def test_update_one_calls_Person_query_get_with_id(self, db_mock, person_mock):
        session_commit_mock = db_mock.session.commit
        query_get_mock = person_mock.query.get
        query_get_mock.return_value = self.p1

        self.people_service.update_one('1', self.p1_input_data)

        session_commit_mock.assert_called_once()
        query_get_mock.assert_called_with('1')

    @patch('app.people_service.Person')
    @patch('app.people_service.db')
    def test_update_one_returns_the_updated_person_data(self, db_mock, person_mock):
        query_get_mock = person_mock.query.get
        query_get_mock.return_value = self.p1

        result = self.people_service.update_one('1', self.p1_input_data)

        self.assertEqual(result, self.p1_output_data)

    @patch('app.people_service.Person')
    @patch('app.people_service.db')
    def test_delete_one_calls_Person_query_get_with_id(self, db_mock, person_mock):
        query_get_mock = person_mock.query.get
        query_get_mock.return_value = self.p1

        self.people_service.delete_one('1')

        query_get_mock.assert_called_with('1')

    @patch('app.people_service.Person')
    @patch('app.people_service.db')
    def test_delete_one_throws_error_when_person_not_found_for_id(self, db_mock, person_mock):
        query_get_mock = person_mock.query.get
        query_get_mock.return_value = None

        with self.assertRaises(ResourceNotFoundError):
            self.people_service.delete_one('1')

    @patch('app.people_service.Person')
    @patch('app.people_service.db')
    def test_delete_one_returns_message(self, db_mock, person_mock):
        query_get_mock = person_mock.query.get
        query_get_mock.return_value = self.p1

        result = self.people_service.delete_one('1')

        self.assertEqual(result, 'Person with id 1 successfully deleted')
