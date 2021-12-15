from sample.register import *
import unittest

class test_Register(unittest.TestCase):

    def setUp(self):
        register = Register([])
        self.tmp = register

    def test_addStudent(self):
        self.assertEqual({"id": 1, "name": "Adam", "surname": "Kowal"},
                         self.tmp.add_Student(1, 'Adam', 'Kowal'))