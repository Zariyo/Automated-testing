import unittest


class Register:
    def __init__(self, students):
        self.students = students

    def get_allStudents(self):
        return self.students

    def get_Student(self, studId):
        for stud in self.students:
            if stud['id'] is studId:
                return stud
        return None

    def add_Student(self, studId, studName, studSurname):
        if self.get_Student(studId) is None:
            if type(studId) is not int:
                if type(studId) in [float, str]:
                    studId = int(float(str(studId)))
                else:
                    raise ValueError("Id must be an integer")
            if type(studName) is not str:
                raise TypeError("Student name must be a string")
            if type(studSurname) is not str:
                raise TypeError("Student surname must be a string")
            self.students.append({"id": studId, "name": studName, "surname": studSurname})
            return self.get_Student(studId)
        else:
            raise Exception("Student ID already taken. Perhaps the student is already in the register?")

    def edit_Student(self, studId, updateId=None, updateName=None, updateSurname=None):
        if type(studId) is not int:
            if type(studId) in [float, str]:
                studId = int(float(str(studId)))
            else:
                raise ValueError("Id must be an integer")
        if type(updateName) is not str:
            raise TypeError("Student name must be a string")
        if type(updateSurname) is not str:
            raise TypeError("Student surname must be a string")
        if type(updateId) is not int and updateId is not None:
            if type(updateId) in [float, str]:
                updateId = int(float(str(updateId)))
            else:
                raise ValueError("Updated Id must be an integer")
        for stud in self.students:
            if stud['id'] is studId:
                if updateId is not None:
                    stud['id'] = updateId
                if updateName is not None:
                    stud['name'] = updateName
                if updateSurname is not None:
                    stud['surname'] = updateSurname
                return stud
        raise Exception("Student with such id does not exist")

    def remove_Student(self, studId):
        if type(studId) is not int:
            if type(studId) in [float, str]:
                studId = int(float(str(studId)))
            else:
                raise ValueError("Id must be an integer")
        i=0
        for stud in self.students:
            if stud['id'] is studId:
                tmp = self.students[i]
                del self.students[i]
                return tmp
            i += 1



