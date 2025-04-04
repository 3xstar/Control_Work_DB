import sqlite3
import random

libraryDB = sqlite3.connect("library.db")
cursor = libraryDB.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS books"
               "(book_id INTEGER,"
               "title TEXT,"
               "author TEXT,"
               "year INTEGER,"
               "available INTEGER)")

cursor.execute("CREATE TABLE IF NOT EXISTS readers"
               "(reader_id INTEGER,"
               "name TEXT,"
               "phone TEXT,"
               "book_id INTEGER)")

libraryDB.close()

def add_book(title, author, year):
    libraryDB = sqlite3.connect("library.db")
    cursor = libraryDB.cursor()
    id = random.randint(1000,9999)

    cursor.execute("INSERT INTO books (book_id,title,author,year, available)" "VALUES (?,?,?,?,?)", (id, title, author, year, 1))

    libraryDB.commit()
    libraryDB.close()

def add_reader(name, phone):
    libraryDB = sqlite3.connect("library.db")
    cursor = libraryDB.cursor()
    id = random.randint(1000, 9999)

    cursor.execute("INSERT INTO readers (reader_id,name,phone)" "VALUES (?,?,?)", (id, name, phone))

    libraryDB.commit()
    libraryDB.close()

def give_book(reader_id, book_id):
    libraryDB = sqlite3.connect("library.db")
    cursor = libraryDB.cursor()

    cursor.execute("UPDATE books SET available=? WHERE book_id=?", (0, book_id))
    cursor.execute("UPDATE readers SET book_id=? WHERE reader_id=?", (book_id, reader_id))

    libraryDB.commit()
    libraryDB.close()

def return_book(book_id):
    libraryDB = sqlite3.connect("library.db")
    cursor = libraryDB.cursor()

    cursor.execute("UPDATE books SET available=? WHERE book_id=?", (1, book_id))
    cursor.execute("UPDATE readers SET book_id=? WHERE book_id=?", ("null", book_id,))

    libraryDB.commit()
    libraryDB.close()

def get_available_books():
    libraryDB = sqlite3.connect("library.db")
    cursor = libraryDB.cursor()

    available_books = cursor.execute("SELECT book_id,title,author,year from books WHERE available=?", (1,))

    print("Список доступных книг:")
    for book in available_books:
        print(book)

    libraryDB.close()

def get_reader_books(reader_id):
    libraryDB = sqlite3.connect("library.db")
    cursor = libraryDB.cursor()

    reader_books_id = cursor.execute("SELECT book_id from readers WHERE reader_id=?", (reader_id,))
    for book_id in reader_books_id:
        book_id = list(book_id)
        searching_books = cursor.execute("SELECT title, author, year from books WHERE book_id=?", ("".join(str(book_id[0])),))
        for book in searching_books:
            print("Книги этого читателя: ", book)
    libraryDB.close()

def search_books(keyword):
    libraryDB = sqlite3.connect("library.db")
    cursor = libraryDB.cursor()

    choice = int(input("Введите по чему искать книгу (1 - по названию / 2 - по автору): "))

    match choice:
        case 1:
            searching_books = cursor.execute("SELECT * from books WHERE title=?", (keyword,))
            for book in searching_books:
                print("Искомая книга: ", book)
        case 2:
            searching_books = cursor.execute("SELECT * from books WHERE author=?", (keyword,))
            for book in searching_books:
                print("Искомая книга: ", book)

    libraryDB.close()

# add_book("лох", "баран", "2007")
# add_reader("чмо", "7895398753")
# give_book(1729, 9617)
# return_book(9617)
get_reader_books(1729)
search_books("баран")