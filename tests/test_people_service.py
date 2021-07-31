import unittest

from app.people_service import PeopleService


class TestPeopleService(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.people_service = PeopleService()
