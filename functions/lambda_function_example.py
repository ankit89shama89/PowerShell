students = [
    {"name": "Ankit", "grade": (90, 67, 89, 90)},
    {"name": "Ashish", "grade": (97, 47, 81, 79)},
    {"name": "Jen", "grade": (70, 87, 93, 87)},
    {"name": "Malen", "grade": (78, 97, 79, 91)},
]

avg = lambda grade: sum(grade) / len(grade)


function_torun = {
    "Average" : avg,
    "Total": lambda grade: sum(grade),
    "Maximum": lambda grade: max(grade)
}

for student in students:
    option = input("Enter the options to perform- Average, Total or Maximum - ")
    function_entered  = function_torun[option]
    value = function_entered(student["grade"])
    print(value)



