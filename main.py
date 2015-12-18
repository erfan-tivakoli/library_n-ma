# encoding: utf-8
__author__ = 'Rfun'
from book import Book
import pickle

books = []
with open('book.pkl', 'r+b') as a:
    books = pickle.load(a)
users = []


def main():
    while True:
        print 'Main Menu'
        print 'Choose your action:'
        print '1-Book Management'
        print '2-Search a book'
        print '3-Personal management'
        print '4-Exit'
        main_action = input()
        main_action = int(main_action)
        if main_action == 1:
            book_management()
        elif main_action == 2:
            search_term = str(input('Please enter the book you want to search:\n'))
            search_in_books(search_term)
        elif main_action == 3:
            personal_management()
        elif main_action == 4:
            print 'Bye bye'
            pickle.dump(books, a)
            break


def book_management():
    while True:
        print 'Choose your action:'
        print '1-Add a new book'
        print '2-Edit an existing book'
        print '3-Delete a book'
        print '4-Search in books'
        print '5-Back to main menu'
        action = input()
        action = int(action)
        if action == 1:
            add_book()
        elif action == 2:
            edit_book()
        elif action == 3:
            delete_book()
        elif action == 4:
            print 'please input your search term'
            search_term = input()
            search_in_books(search_term)
        elif action == 5:
            break


def add_book():
    'TODO : id unification'

    id = str(input('Enter book id \n'))
    name = input('Enter book name \n')
    quantity = str(input('Enter number of books\n'))

    b = Book(id, name, quantity)
    print 'book has been saved'
    books.append(b)


def edit_book():
    search_term = str(input('Please enter the book you want to edit:\n'))
    search_result = search_in_books(search_term)
    print 'Your search results are:'
    for b in search_result:
        print b
    id = str(input('please enter your choice id:\n'))
    for book in books:
        if book.id == id:
            chosen_book = book

    print 'Enter your edition field:'
    while True:
        print '1-id'
        print '2-name'
        print '3-quantity'
        print '4-exit'
        field = input()
        field = int(field)
        if field == 1:
            print 'Enter new id:'
            new_id = input()
            chosen_book.update_id(new_id)
        elif field == 2:
            print 'Enter new name:'
            new_name = input()
            chosen_book.update_name(new_name)
        elif field == 3:
            print 'Enter new quantity:'
            new_qt = input()
            chosen_book.update_id(new_qt)
        elif field == 4:
            break
        print_all()


def delete_book():
    search_term = str(input('Please enter the book you want to delete:\n'))
    search_result = search_in_books(search_term)
    print 'Your search results are:'
    for b in search_result:
        print b
    id = str(input('please enter your choice id:\n'))
    for book in books:
        if book.id == id:
            books.remove(book)
    print_all()


def search_in_books(search_term):
    search_result = []
    for book in books:
        if book.name.__contains__(search_term) or book.id.__contains__(search_term):
            search_result.append(book)
    print_all(search_result)
    return search_result


def print_all(list=books):
    print 'list of all books: '
    for book in list:
        print book
    if len(list) == 0:
        print 'There is nothing to display'

def personal_management():
    while True:
        print 'choose your action:'
        print '1-add new member'
        print '2-edit member'
        print '3-borrow book'
        print '4-return book'
        print '5-report of latencies'
        

if __name__ == '__main__':
    main()