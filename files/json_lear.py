import json

file = open('json.txt', 'r')
content = json.load(file)
file.close()

print(content)

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Maruti', 'model': 'Swift'}
]

file_data = open('nearby.txt', 'w')
data = json.dump(cars, file_data)
file_data.close()