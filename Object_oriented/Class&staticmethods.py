class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

para = Foo()

para.hi()

class bar:
    @staticmethod
    def hi():
        print("I do not take any parameters")

para1 = bar()
para1.hi()

#### second example
class Floatnumber:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    @classmethod
    def from_sum(cls, number1, number2):
        return cls(number1 + number2)

class Euro(Floatnumber):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "€"

    def __repr__(self):
        return f"<Euro {self.symbol}{self.amount:.2f}>"


new_number = Floatnumber.from_sum(2.345, 4.562)
print(new_number)

new_euro = Euro.from_sum(2.345, 4.562)
print(new_euro)