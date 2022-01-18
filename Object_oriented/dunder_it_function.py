students = {
    "name": "Ankit Sharma",
    "grades": [70, 90, 89, 90, 98]
}

def average(seq):
    return sum(seq) / len(seq)


class Mystudents:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def avg(self):
        avg = sum(self.grades) / len(self.grades)
        print(avg)


student_one = Mystudents("Ankit Sharma", [70, 90, 89, 90, 98])

print(student_one.avg())

###### advance dunder class
class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, index):
        return self.cars[index]

    def __repr__(self):
        return f'Garage {self.cars}'

    def __str__(self):
        return f'Garage has {len(self)} cars'

ford = Garage()
ford.cars.append("Mustang")
ford.cars.append("Fiat")
ford.cars.append("Fieta")
print(len(ford))

print(ford[0])  ### Garage.__getitem__.(ford, 0)

print(ford)

######third example
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __str__(self):
        return f'Club {self.name}: {self.players}'

    def __getitem__(self, index):
        return self.players[index]

c_club = Club("MNC")

c_club.players.append("Ankit")
c_club.players.append("Kartik")
c_club.players.append("Ashish")

print(c_club[0])
print(c_club)