from sample.register import *
import unittest

class test_Register(unittest.TestCase):

    def setUp(self):
        register = Register([])
        self.tmp = register
        self.tmp.add_Student(2, 'Krzysztof', 'Kowal')

    def test_addStudent(self):
        self.assertEqual({"id": 1, "name": "Adam", "surname": "Kowal"},
                         self.tmp.add_Student(1, 'Adam', 'Kowal'))

    def test_addStudent_exception_studentExists(self):
        self.assertRaises(Exception, self.tmp.add_Student, 2, 'Krzysztof', 'Kowal')

    def test_addStudent_exception_id_not_int(self):
        self.assertRaises(ValueError, self.tmp.add_Student, "abc", 'Adam', 'Nowak')

    def test_addStudent_id_as_float(self):
        self.assertEqual({"id": 1, "name": "Adam", "surname": "Kowal"},
                         self.tmp.add_Student(1.0, 'Adam', 'Kowal'))

    def test_addStudent_id_as_string(self):
        self.assertEqual({"id": 1, "name": "Adam", "surname": "Kowal"},
                         self.tmp.add_Student("1.0", 'Adam', 'Kowal'))