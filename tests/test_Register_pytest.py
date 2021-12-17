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

