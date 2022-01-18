class fixedfloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<fixedfloat {self.amount:.2f}>'
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)

class euro(fixedfloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'
    def __repr__(self):
        return f'<euro {self.symbol}{self.amount:.2f}>'

money = euro(13.786)
print(money)
sum_money = money.from_sum(123.345, 23.674)
print(sum_money)


