import re

from app.constants import PERSON_KEYS, SORT_REGEX
from app.error import ValidationError


class Validator:

    @staticmethod
    def check_add_request(data: dict) -> None:
        missing = [k for k in PERSON_KEYS if k not in data.keys()]

        if len(missing) > 0:
            raise ValidationError(f'Missing keys in request: {missing}')

    @staticmethod
    def check_sort_key(key: str) -> (bool, str):
        """
        Validate sort key against regex and then check it is valid against expected keys
        :param key: sort key looks like: '-name' or 'name' for descending or ascending sort respectively
        :return: Bool to indicate if sign (-) was found and the key without sign
        """
        if not re.search(SORT_REGEX, key):
            raise ValidationError(f'Unrecognised format for sort parameter: [{key}]. Expected format like -name')

        has_sign, signless_key = (False, key) if key[0:1] != '-' else (True, key[1:])

        if signless_key.lower() not in PERSON_KEYS:
            raise ValidationError(f'Cannot sort on [{key}]. Must be one of the following: {PERSON_KEYS}.')

        return has_sign, signless_key

    @staticmethod
    def check_update_request(data: dict) -> None:
        invalid = [k for k in data.keys() if k not in PERSON_KEYS]

        if len(invalid) > 0:
            raise ValidationError(f'Invalid keys found in request: {invalid}')
