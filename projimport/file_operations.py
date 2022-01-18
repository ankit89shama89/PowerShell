def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

if __name__ == "__main__":
    test = read_from_file('data.txt')
    print(test)

print(__name__)