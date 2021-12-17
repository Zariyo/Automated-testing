from parameterized import parameterized, parameterized_class
from sample.register import *
import unittest
import pytest


register = Register([])
reg = register
reg.add_Student(2, 'Krzysztof', 'Kowal')
reg.add_Student(28, 'Adam', 'Nowak')
reg.add_Student(42, 'Jan', 'Kowalski')
reg.add_subject(42, 'geography')
reg.add_Student(55, 'Kamil', 'Stoszek')
reg.add_subject(55, 'maths')
reg.add_notes(55, 'maths', [4,6,2,3.5])
reg.add_subject(55, 'geography')
reg.add_notes(55, 'geography', [1,2,3])

def test_add_student():
    assert reg.add_Student(3, "Ewa", "Robak") == {"id": 3, "name": "Ewa", "surname": "Robak", "subjects": [], "notices": []}

def test_add_student_exception():
    with pytest.raises(Exception):
        reg.add_Student("ab", "Jan", "Robak")

def test_edit_student():
    assert reg.edit_Student(2, None, "Patryk", None) == {"id": 2, "name": "Patryk", "surname": "Kowal", "subjects": [], "notices": []}

def test_edit_student_exception():
    with pytest.raises(Exception):
        reg.edit_Student(2, None, 12, None)

def test_remove_student():
    assert reg.remove_Student(2) == {"id": 2, "name": "Patryk", "surname": "Kowal", "subjects": [], "notices": []}

def test_remove_student_exception():
    with pytest.raises(Exception):
        reg.remove_Student("O")

def test_add_subject():
    assert reg.add_subject(28, "maths") == {"id": 28, "name": "Adam", "surname": "Nowak", "subjects": [{"subject": "maths", "notes": []}], "notices": []}

def test_add_subject_exception():
    with pytest.raises(Exception):
        reg.add_subject(28, "mathematics")