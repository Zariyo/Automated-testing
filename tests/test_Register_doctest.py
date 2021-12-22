from sample.register import *
import unittest

register = Register([])
reg = register
reg.add_Student(2, 'Krzysztof', 'Kowal')
reg.add_Student(28, 'Adam', 'Nowak')
reg.add_Student(42, 'Jan', 'Kowalski')
reg.add_subject(42, 'geography')
reg.add_Student(55, 'Kamil', 'Stoszek')
reg.add_subject(55, 'maths')
reg.add_notes(55, 'maths', [4, 6, 2, 3.5])
reg.add_subject(55, 'geography')
reg.add_notes(55, 'geography', [1, 2, 3])

def test_WithDocRegister(self):
    """
    >>> reg.add_Student(3, "Jan", "Dab")
    {"id": 3, "name": "Jan", "surname": "Dab", "subjects": [], "notices": []}
    >>> reg.edit_Student(2, None, "Maria", None)
    {"id": 2, "name": "Maria", "surname": "Kowal", "subjects": [], "notices": []}
    >>> reg.add_subject(2, "maths")
    {"id": 2, "name": "Maria", "surname": "Kowal", "subjects": ["subject": "maths", "notes": []], "notices": []}
    """





if __name__ == "__main__":
    import doctest
    doctest.testmod()