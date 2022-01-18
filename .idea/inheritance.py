class student:
    def __init__(self, name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

class Workingstudent(student):
    def __init__(self, name,school,salary):
        super().__init__(name,school)
        self.salary = salary
    def weekly_salary(self):
        return self.salary * 7


rolf = Workingstudent('rolf',"hans raj",18.60)
rolf.marks.append(78)
rolf.marks.append(89)
print(" Rolf Data")
print(rolf.school)
print(rolf.salary)
print(rolf.average_marks())

#######decorater #############
###making no argument method into property ## weekly_salary
class Workingstud(student):
    def __init__(self, name,school,salary):
        super().__init__(name,school)
        self.salary = salary
    @property
    def weekly_salary(self):
        return self.salary * 7

print("norm Data")
norm = Workingstud('norm',"MIT",11.60)
norm.marks.append(78)
norm.marks.append(89)
print(norm.school)
print(norm.salary)
print(norm.weekly_salary)