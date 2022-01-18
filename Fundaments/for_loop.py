## foreach in powerShell

for i in range(3,10):
    print("hello, we have moved to the queue -", i)

##### 2nd prog
students = [
    {"name": "Ankit", "grade": 84},
    {"name": "Ashish", "grade": 90},
    {"name": "Jen", "grade": 72},
    {"name": "Malen", "grade": 67},
]

for stud in students:
    print(stud["name"], "-", stud["grade"])

##### 3rd list\tuples
friends = [("Rolf", 32), ("jen", 21)]

for name, age in friends:
    print(f"{name} is {age} years old.")

friends = {"Rolf": 32, "jen": 21}

##### for with dictionary
for name, age in friends.items():
    print(f"{name} is {age} years old.")

##### for loop with break and else
cars = ["ok", "ok", "ok", "ok", "ok"]

for car in cars:
    if car == "faulty":
        print("This cars is having status -", car)
        break
    print("This cars is having status -", car)
    print("Ship the car to the customer")
else:
    print("All cars built successfully. No faulty cars!")

### new list for existing using for loop
numbers = [1, 2, 3, 4, 5]
new_num = [ _ * 2 for _ in numbers]
print(new_num)

###Example 2
friends = ["Ank", "jos"]
lower_friends = [ _.lower() for _ in friends]
user = input("Enter your name: ")

if user.lower() in lower_friends:
    print( user.title(), "is a friend" )

## example 3
friends = ["rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "bob", "Rolf", "Charlie", "michael", "JEN"]
guests_lower = [ _.lower() for _ in guests]
intersection = [ _.title() for _ in friends if _.lower() in guests_lower ]

print(intersection)