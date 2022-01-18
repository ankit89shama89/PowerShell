class Car():
    def __init__(self, name, make):
        self.name = name
        self.make = make

    def __repr__(self):
        return f'Car {self.name}: {self.make}'

class Garage():
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a {car.__class__.__name__} to the garage")
        self.cars.append(car)


Ford = Car('fiesta', '1987')
Fiesta = Garage()

try:
    Fiesta.add_car("Fiesta")
except ValueError:
    print("Your car was not made of Car class")
except TypeError:
    print("Your car was not made of Car class")
finally:
    print(len(Fiesta))

