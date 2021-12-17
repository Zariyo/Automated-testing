import unittest
from hamcrest import *
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

    def test_add_student_equals(self):
        assert_that(self.tmp.add_Student(1, 'Adam', 'Kowal'), equal_to({"id": 1, "name": "Adam", "surname": "Kowal", "subjects": [], "notices": []}))

    def test_edit_student_is_object(self):
        assert_that(self.tmp.edit_Student(2, 15, "Karol", "Wojtylski"), is_(object))

    def test_add_subject_has_entry(self):
        assert_that(self.tmp.add_subject(2, "maths"), has_entry("subjects", [{"subject": "maths", "notes": []}]))

    def test_add_notes_has_value(self):
        assert_that(self.tmp.add_notes(42, "geography", [1,2,3,4]), has_value([{'subject': 'geography', 'notes': [1, 2, 3, 4]}]))

    def test_add_behavior_notice_not_None(self):
        assert_that(self.tmp.add_behavior_notice(2, "Bad language"), not_none())

    def test_edit_subject_exception_subject_not_taught(self):
        assert_that(calling(self.tmp.edit_subject).with_args(2, "maths", "german"), raises(Exception))

