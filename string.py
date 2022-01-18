###### string function

name = 'ANkit'
string = f"this is the string {name}"
name = "pankaj"
print(string)

#########Advance
name = 'ANkit'
string = "this is the string {}"
greet = string.format(name)
name = "Akas"
print(greet)

#####most advance
name = 'ANkit'
string = "this is the string {name}"
greet = string.format(name=name)
name = "Akas"
print(string.format(name=name))

########### user input
name = "Ankit"
user_name = input("Enter your name:")
print(f"hello {user_name}, my name is {name}")

###SUM, length and Average

list = [23,34,4,45,35]

total = sum(list)
length = len(list)
Average = sum(list) / len(list)

print(total)
print(length)
print(Average)

######## print integer with integer as input
user_name = input("Enter your name:  ")
user_age = int(input("Enter your age:  "))
print(f'hello {user_name}, your life in months is {user_age * 12 *30 * 24 * 60* 60} seconds')

#########  comparisons
age = int(input("enter random number:  "))
check = 20
check_age = age <= check
print(f"the statement Age {age} is less than {check} - {check_age}")

#####List
list = [["wer",20], ["bob",34], ["wer",31]]
list.append(["amkit" ,29])
list.remove(["wer", 20])
print(list[0][0])

Join List


##tupple
tuple = "asd" , "wer"
clear_tuple = ("asd" , "wer")
tuple_in_list = [("asd" , "wer")]

print(tuple)
print(clear_tuple)
print(tuple_in_list)

### Adding entry in tuple
tuple = ("asd" , "wer")
tuple = tuple + ("Jen","wer")
print(tuple)

###sets  
art = {"rolf", "Ank"}
sci = {"rolf", "jen", "wer"}
art_not_sci = art.difference(sci)
sci_not_sci = sci.difference(art)

not_in_both = art.symmetric_difference(sci)
unique = art.union(sci)

print(art_not_sci)
print(sci_not_sci)

print(not_in_both)
print(unique)

###Dictionary

friends_ages = {"Rolf" : 24, "ser" : 12}
print(friends_ages["Rolf"])

##Setting values
friends_ages["Rolf"] = 21
friends_ages["use"] = 45
print(friends_ages["use"])

##list to disctionary

list = [("rolf", 24),("Adam", 34),("ANk",29)]
dict = dict(list)
print(dict)

######### Summation of list,tuple, set        #############################################

list = [["wer",20], ["bob",34], ["wer",31]]     ########## List
tuple = ("asd" , "wer")                         ########## Tuple
set = {"rolf", "Ank"}                           ########### Set
dict = {"Rolf" : 24, "ser" : 12}                ############ Dictionary           


lottery_numbers = {13, 21, 22, 5, 8}

############# List join
list = ["Ankit", "Manish", "Abnjw"]
separated = ", ".join(list)
print(f"My friends list are {separated}.")



