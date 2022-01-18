class User:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f'User {self.name}'

def find_percent(user):
    max_marks = user.marks["max"]
    obtain_marks = user.marks["obtain"]
    percent = (obtain_marks * 100) / max_marks
    return percent

def user_percent(user):
    try:
        percent = find_percent(user)
    except KeyError:
        print("Incorrect values provided to calculation function")
        raise
    else:
        print(f"User {user.name} got {percent}% marks")


my_user = User("Ankit", {"max": 90, "obtain": 81})
user_percent(my_user)

