import unittest


class Register:
    def __init__(self, students):
        self.students = students

    def get_allStudents(self):
        return self.students

    def get_Student(self, studId):
        for stud in self.students:
            if stud['id'] == studId:
                return stud
        return None

    def add_Student(self, studId, studName, studSurname):
        if self.get_Student(studId) is None:
            self.students.append({"id": studId, "name": studName, "surname": studSurname})
            return self.get_Student(studId)
        else:
            raise Exception("Student ID already taken. Perhaps the student is already in the register?")

