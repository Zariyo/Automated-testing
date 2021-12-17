import unittest
from assertpy import *
from sample.register import *
import unittest

class test_Register_PyHamcrest(unittest.TestCase):
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

    def test_add_student_is_equal(self):
        assert_that(self.tmp.add_Student(12, "Jan", "Wisniewski")).is_equal_to({"id": 12, "name": "Jan", "surname": "Wisniewski", "subjects": [], "notices": []})

    def test_edit_student_is_instance_of_object(self):
        assert_that(self.tmp.edit_Student(2,None, "Janek", "Wisnia")).is_instance_of(object)

    def test_edit_student_is_iterable(self):
        assert_that(self.tmp.edit_Student(2,None, "Janek", "Wisnia")).is_iterable()

    def test_add_subject_contains_entry(self):
        assert_that(self.tmp.add_subject(2, "maths")).contains_entry({'subjects': [{'subject': 'maths', 'notes': []}]})

    def test_edit_subject_contains_value(self):
        assert_that(self.tmp.edit_subject(55, "maths", "physics")).contains_value([{'subject': 'physics', 'notes': [4, 6, 2, 3.5]}, {'subject': 'geography', 'notes': [1, 2, 3]}])

