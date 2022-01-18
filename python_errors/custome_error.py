def count_from_zero_to_n(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    for x in range(0, n+1):
        print(x)

count_from_zero_to_n(0)

### error with codes
class MyCustomError(TypeError):
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

raise MyCustomError('This error occurred', 500)

#### 2nd Example
class UncountableError(ValueError):
    def __init__(self, n):
        super().__init__(f'Invalid value for {n},WRONG_VALUE. n must be a greater than 0')



def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)

n = int(input("enter one number- "))
count_from_zero_to_n(n)