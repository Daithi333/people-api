import unittest

from app import ValidationError
from app.validator import Validator


class TestValidator(unittest.TestCase):
    valid_add_request = {
        "address": "616 Park Royal, Belfast, BT4FGL",
        "age": 55,
        "balance": 12303.0,
        "email": "jimmym@somemail.com",
        "name": "Jim Morrison"
      }
    invalid_add_request = {"name": "Jim Morrison"}
    invalid_update_request = {"id": 7}

    def test_check_add_request_does_not_raise_error_when_request_valid(self):
        try:
            Validator.check_add_request(self.valid_add_request)
        except ValidationError:
            self.fail('An Exception was raised!')

    def test_check_add_request_raises_error_when_keys_missing(self):
        with self.assertRaises(ValidationError):
            Validator.check_add_request(self.invalid_add_request)

    def test_check_sort_key_raises_error_when_key_format_is_incorrect(self):
        with self.assertRaises(ValidationError):
            Validator.check_sort_key('--name')

    def test_check_sort_key_raises_error_when_key_format_is_incorrect_2(self):
        with self.assertRaises(ValidationError):
            Validator.check_sort_key('-123')

    def test_check_sort_key_raises_error_when_key_is_not_in_expected_list(self):
        with self.assertRaises(ValidationError):
            Validator.check_sort_key('invalid')

    def test_check_sort_key_returns_expected_response_when_sign_in_key(self):
        sign, key = Validator.check_sort_key('-name')
        self.assertEqual(sign, True)
        self.assertEqual(key, 'name')

    def test_check_sort_key_returns_expected_response_when_no_sign_in_key(self):
        sign, key = Validator.check_sort_key('name')
        self.assertEqual(sign, False)
        self.assertEqual(key, 'name')

        try:
            Validator.check_update_request(self.valid_add_request)
        except ValidationError:
            self.fail('An Exception was raised!')

    def test_check_update_request_raises_error_when_keys_missing(self):
        with self.assertRaises(ValidationError):
            Validator.check_update_request(self.invalid_update_request)
