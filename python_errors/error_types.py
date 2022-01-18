"""
Type of Errors in python
1. Index Error
2. Key Error
3. Name Error
4. Attribute error
5. NotimplementedError
6. Indentation Error - No example
7. Tab Error  - No example
8. TypeError - No example
9. valueError
"""


#### Index error
friends = ["Ankit", "Ashish"]
print(friends[2])

"""
Traceback (most recent call last):
File "C:\temp\python\python_errors\general.py", line 4, in <module>
print(friends[2])
IndexError: list index out of range
"""

### Key error
dictionary = { "Name": "DDLJ",
               "year": 1996,
               "Director": "subhash ghai"
               }
print(dictionary["release"])
"""
Traceback (most recent call last):
  File "C:\temp\python\python_errors\general.py", line 7, in <module>
    print(dictionary["release"])
KeyError: 'release'
"""

## NameError
print(Friends)

"""
Traceback (most recent call last):
  File "C:\temp\python\python_errors\general.py", line 3, in <module>
    print(Friends)
NameError: name 'Friends' is not defined
"""

### Attribute error
Friends = ["Ankit", "rolf", "pan"]
Family = ["Ankit", "James", "Jan"]
Friends.intersection(Family)

"""
Traceback (most recent call last):
  File "C:\temp\python\python_errors\general.py", line 4, in <module>
    Friends.intersection(Family)
AttributeError: 'list' object has no attribute 'intersection'
"""

#### NotimplementedError
class User:
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def login(self):
        raise NotImplementedError('This Feature is in progress')

Ankit = User("ankit", "werrde" )
Ankit.login()

"""
Traceback (most recent call last):
  File "C:\temp\python\python_errors\general.py", line 13, in <module>
    Ankit.login()
  File "C:\temp\python\python_errors\general.py", line 9, in login
    raise NotImplementedError('This Feature is in progress')
NotImplementedError: This Feature is in progress
"""

### value error
int('10.7')

"""
Traceback (most recent call last):
  File "C:\temp\python\python_errors\general.py", line 2, in <module>
    int('10.7')
ValueError: invalid literal for int() with base 10: '10.7'
"""