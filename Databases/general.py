from database import read_bookdata, add_book, mark_read, remove_book
bookdb_file = 'bookdb.txt'
value = 1

def menu_option():
    print('=============================================================')
    print(' User Menu Options are as below -')
    print('1. List Book                        2. Add Book')
    print('3. Mark Read                        4. Delete Book')
    user_input = input('Please enter one option (q for quite)- ')
    return user_input
    print('Please enter the correct option -')


print('=============================================================')
print('=============  Welcome to the Book store  ===================')
print('=============================================================')

while value == 1:
    user_input = menu_option()

    if user_input == '1':
        book_DB = read_bookdata(bookdb_file)
        for i in range(len(book_DB)):
            Name = book_DB[i]['name']
            Author = book_DB[i]['author']
            Read = book_DB[i]['read']
            no = i + 1
            print(f'{no}. Name - {Name}, Author - {Author}, Read - {Read}')

    elif user_input == '2':
        add_book(bookdb_file)

    elif user_input == '3':
        book_name = input('Please enter the book name - ')
        mark_read(book_name, bookdb_file)

    elif user_input == '4':
        remove_book(bookdb_file)

    elif user_input == 'q':
        value = 0

    else:
        print('Please enter the correct option -')










