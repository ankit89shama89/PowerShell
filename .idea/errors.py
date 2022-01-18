class Garage():
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_cars(self, car):
        raise NotImplementedError(" We can't add cars to garage yet")


ford = Garage()
ford.add_cars('Maryit')
