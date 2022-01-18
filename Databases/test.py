import json
bookdb_file = 'bookdb.txt'

def read_bookdata(filename):
    with open(filename, 'r') as file:
        content = json.load(file)
        return content

def write_bookdata(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def mark_read(name, filename):
    found = 0
    book_DB = read_bookdata(filename)
    print(book_DB[0])
    for i in range(len(book_DB)):
        print(i)
        print(book_DB[i]['name'])
        if book_DB[i]['name'] == name:
            found = 1
            if book_DB[i]['read'] == False:
                book_DB[i]['read'] = True
                print(f'Book with name {name} is marked as read')
                write_bookdata(filename, book_DB)
                break
            else:
                print(f'Book with name {name} is already marked as read')
                break

    if found == 0:
        print(f'Book with name {name} is not found')

mark_read('3idiot', bookdb_file)