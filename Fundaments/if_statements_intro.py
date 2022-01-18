##first prog
num = input("Enter any number: ")
num = int(num)

if num > 10:
    print(num, "is greater than 10")
else:
    print(num, "is less than or equal to 10")

print("exit")

#### second prog
frnds = ["Ankit", "ashish", "kartik"]
family = ["Any", "jen"]
user_name = input("Enter your name: ")

if user_name in frnds:
    print("Hello Friend!", user_name)
elif user_name in family:
    print("Hello Family!", user_name)
else:
    print("We don't know you", user_name)