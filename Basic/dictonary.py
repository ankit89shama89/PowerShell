dict = {"ank": 24, "awe": 21, "aqs": 31 }
print(dict["ank"])

### addition and assignment in dictionary
dict["acd"] = 43
dict["ank"] = 10
print(dict)

#### dictionary with tupple

friends = (
    {"name": "ank", "age": 24},
    {"name": "asd", "age": 12},
    {"name": "aqw", "age": 31}
)

print("Age of the user", friends[0]["name"]," is", friends[0]["age"])

#### len and sum
grades = [90, 45, 41, 90]
print(len(grades))
print(sum(grades))

########## joining list
friends = ["ankit", "ashish", "kartik"]
join_grades = ", ".join(friends)
print("My marks are - ", join_grades)





