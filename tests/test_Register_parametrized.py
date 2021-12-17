from parameterized import parameterized, parameterized_class
from sample.register import *
import unittest

class TestAgeCalc(unittest.TestCase):
    def setUp(self):
        register = Register([])
        self.tmp = register
        self.tmp.add_Student(2, 'Krzysztof', 'Kowal')
        self.tmp.add_Student(28, 'Adam', 'Nowak')
        self.tmp.add_Student(42, 'Jan', 'Kowalski')
        self.tmp.add_subject(42, 'geography')
        self.tmp.add_Student(55, 'Kamil', 'Stoszek')
        self.tmp.add_subject(55, 'maths')
        self.tmp.add_notes(55, 'maths', [4,6,2,3.5])
        self.tmp.add_subject(55, 'geography')
        self.tmp.add_notes(55, 'geography', [1,2,3])

    @parameterized.expand([
        (10, "Adam", "Janowski", {"id": 10, "name": "Adam", "surname": "Janowski", "subjects": [], "notices": []}),
        (11, "Jan", "Adamowski", {"id": 11, "name": "Jan", "surname": "Adamowski", "subjects": [], "notices": []}),
        (13, "Przemyslaw", "Piotrowski", {"id": 13, "name": "Przemyslaw", "surname": "Piotrowski", "subjects": [], "notices": []}),
        (14, "Piotr", "Przemyslowski", {"id": 14, "name": "Piotr", "surname": "Przemyslowski", "subjects": [], "notices": []})
    ])

    def test_parametrized_add_student(self, studId, studName, studSurname, expectedOutput):
        self.assertEqual(self.tmp.add_Student(studId, studName, studSurname), expectedOutput)

    @parameterized.expand([
        ("ab", "Adam", "Janowski"),
        ({}, "Jan", "Adamowski"),
        ([], "Przemyslaw", "Piotrowski"),
        (None, "Piotr", "Przemyslowski")
    ])

    def test_parametrized_add_student_exceptions_bad_id(self, studId, studName, studSurname):
        self.assertRaises(ValueError, self.tmp.add_Student,studId, studName, studSurname)

    @parameterized.expand([
        ("2", None, "Krzysiu", "Kowalski", {"id": 2, "name": "Krzysiu", "surname": "Kowalski", "subjects": [], "notices": []}),
        (42, 43, "Janek", "Kowal", {"id": 43, "name": "Janek", "surname": "Kowal", "subjects": [{'notes': [], 'subject': 'geography'}], "notices": []}),
        (55, None, None, "Stoch", {"id": 55, "name": "Kamil", "surname": "Stoch", "subjects": [{'notes': [4, 6, 2, 3.5], 'subject': 'maths'},
              {'notes': [1, 2, 3], 'subject': 'geography'}], "notices": []})
    ])

    def test_parametrized_edit_student(self, studId, updId, updName, updSurname, expectedOutput):
        self.assertEqual(self.tmp.edit_Student(studId, updId, updName, updSurname), expectedOutput)