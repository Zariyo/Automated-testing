from sample.register import *
import unittest


class test_Register(unittest.TestCase):

    def setUp(self):
        register = Register([])
        self.tmp = register
        self.tmp.add_Student(2, 'Krzysztof', 'Kowal')
        self.tmp.add_Student(28, 'Adam', 'Nowak')

    def test_add_Student(self):
        self.assertEqual({"id": 1, "name": "Adam", "surname": "Kowal", "subjects": []},
                         self.tmp.add_Student(1, 'Adam', 'Kowal'))

    def test_add_Student_exception_studentExists(self):
        self.assertRaises(Exception, self.tmp.add_Student, 2, 'Krzysztof', 'Kowal')

    def test_add_Student_exception_id_not_int(self):
        self.assertRaises(ValueError, self.tmp.add_Student, "abc", 'Adam', 'Nowak')

    def test_add_Student_id_as_float(self):
        self.assertEqual({"id": 1, "name": "Adam", "surname": "Kowal", "subjects": []},
                         self.tmp.add_Student(1.0, 'Adam', 'Kowal'))

    def test_add_Student_id_as_string(self):
        self.assertEqual({"id": 1, "name": "Adam", "surname": "Kowal", "subjects": []},
                         self.tmp.add_Student("1.0", 'Adam', 'Kowal'))

    def test_add_Student_exception_id_as_None(self):
        self.assertRaises(ValueError, self.tmp.add_Student, None, 'Adam', 'Nowak')

    def test_add_Student_exception_id_as_empty_list(self):
        self.assertRaises(ValueError, self.tmp.add_Student, [], 'Adam', 'Nowak')

    def test_add_Student_exception_id_as_empty_object(self):
        self.assertRaises(ValueError, self.tmp.add_Student, {}, 'Adam', 'Nowak')

    def test_add_Student_exception_name_not_string(self):
        self.assertRaises(TypeError, self.tmp.add_Student, 4, 15, 'Nowak')

    def test_add_Student_exception_surname_not_string(self):
        self.assertRaises(TypeError, self.tmp.add_Student, 4, 'Adam', 20)

    def test_edit_Student(self):
        self.assertEqual({"id": 2, "name": "Krzysiek", "surname": "Kowalski", "subjects": []},
                         self.tmp.edit_Student(2, None, "Krzysiek", "Kowalski"))

    def test_edit_Student_exception_noStudent(self):
        self.assertRaises(Exception, self.tmp.edit_Student, 15, None, "Adam", "Kamien")

    def test_edit_Student_exception_id_not_int(self):
        self.assertRaises(Exception, self.tmp.edit_Student, "abc", None, "Adam", "Kamien")

    def test_edit_Student_exception_id_as_empty_list(self):
        self.assertRaises(ValueError, self.tmp.edit_Student, 15, [], "Adam", "Kamien")

    def test_edit_Student_exception_id_as_empty_object(self):
        self.assertRaises(ValueError, self.tmp.edit_Student, 15, {}, "Adam", "Kamien")

    def test_edit_Student_exception_name_not_string(self):
        self.assertRaises(TypeError, self.tmp.edit_Student, 15, None, 123, "Kamien")

    def test_edit_Student_exception_surname_not_string(self):
        self.assertRaises(TypeError, self.tmp.edit_Student, 15, None, "Adam", 123)

    def test_remove_Student(self):
        self.assertEqual({"id": 28, "name": "Adam", "surname": "Nowak", "subjects": []}, self.tmp.remove_Student(28))

    def test_remove_Student_id_not_int(self):
        self.assertRaises(ValueError, self.tmp.remove_Student, "abc")

    def test_remove_Student_no_student(self):
        self.assertRaises(Exception, self.tmp.remove_Student, 100)

    def test_add_subject(self):
        self.assertEqual(
            {"id": 2, "name": "Krzysztof", "surname": "Kowal", "subjects": [{"subject": "maths", "notes": []}]},
            self.tmp.add_subject(2, "maths"))

    def test_add_subject_exception_no_subject(self):
        self.assertRaises(Exception, self.tmp.add_subject, 2, "spanish")
