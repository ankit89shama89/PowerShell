## define simple function
def simplefun():
    name = input("Enter your name: ")
    print("Hello Sir! -", name)

simplefun()

### function with parameter
cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 458},
    {"make": "Ford", "model": "Mx-5", "mileage": 21000, "fuel_consumed": 502},
    {"make": "Ford", "model": "swat", "mileage": 29000, "fuel_consumed": 340},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 278},
]

def calculate_mileage(car):
    mpg = car["mileage"]/car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(name, "does", mpg, "miles per gallon")

for car in cars:
    calculate_mileage(car)

#### function with return value
cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 458},
    {"make": "Ford", "model": "Mx-5", "mileage": 21000, "fuel_consumed": 502},
    {"make": "Ford", "model": "swat", "mileage": 29000, "fuel_consumed": 340},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 278},
]

def find_mileage(car):
    mileage = car["mileage"]/car["fuel_consumed"]
    return mileage

def find_name(car):
    name = f"{car['make']} {car['model']}"
    return name

def calculate_mpg(car):
    mpg = find_mileage(car)
    name = find_name(car)
    print(name, "does", mpg, "miles per gallon")

for car in cars:
    calculate_mpg(car)

### lambda function

divide = lambda x,y: x / y
print(divide(4, 2))