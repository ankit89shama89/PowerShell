class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class StudentInfo(Student):

    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


first_student = StudentInfo("Ankit", "RPVV", 14.6)

first_student.marks.append(98)
first_student.marks.append(78)
first_student.marks.append(88)

print(first_student.salary)
print(first_student.name)
print(first_student.marks)
print(first_student.average())


############################ function as a property
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class StudentInfo(Student):

    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 7


first_student = StudentInfo("Ankit", "RPVV", 14.6)
first_student.marks.append(98)
first_student.marks.append(78)
first_student.marks.append(88)
print(first_student.salary)
print(first_student.name)
print(first_student.marks)
print(first_student.weekly_salary)