import json

def write_bookdata(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def read_bookdata(filename):
    with open(filename, 'r') as file:
        content = json.load(file)
        return content


def add_book(filename):
    name = input('Enter the book name - ')
    author = input('Enter the author name - ')
    book_list = {'name': name, 'author': author, 'read': False}
    book_DB = read_bookdata(filename)
    book_DB.append(book_list)
    write_bookdata(filename, book_DB)

def mark_read(name, filename):
    found = 0
    book_DB = read_bookdata(filename)
    for book in book_DB:
        if book['name'] == name:
            found = 1
            if book['read'] == False:
                book['read'] = True
                print(f'Book with name {name} is marked as read')
                write_bookdata(filename, book_DB)
            else:
                print(f'Book with name {name} is already marked as read')
        break
    if found == 0:
        print(f'Book with name {name} is not found')

def remove_book(filename):
    name = input('Enter the book name to delete - ')
    found = 0
    book_DB = read_bookdata(filename)
    for i in range(len(book_DB)):
        if book_DB[i]['name'] == name:
            found = 1
            book_DB.remove(book_DB[i])
            write_bookdata(filename, book_DB)
            print(f"We have removed book {name} from Database")
            break
    if found == 0:
        print(f"We didn't found book {name} in Database")

print("Imported module test_mo successfully")
