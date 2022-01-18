#### variables and numbers
age = 35
print(age)

age_new = age + 5
age_new_str = str(age_new)
print("the new age of the person is", age_new)
print("the new age of the person is " + age_new_str)

###### Strings and escaping
name = "An\"ki\"t"
string = "Hello, world!"
print(string, "This 'is your host'", name)

multipleline = """ Hello World!.
This is Ankit , your new host.
Byee

"""
print(multipleline)

##### F strings in print
name = "Ankit"
greeting = f"How are you, {name}?"
print(greeting)

##### string formatting on a go

name = "jose"
greeting = "How are you, {}?"
print(greeting.format(name))
name = "Ankit"
print(greeting.format(name))



