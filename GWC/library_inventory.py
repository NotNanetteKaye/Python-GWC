from books import Books


class Library_Inventory:
    def __init__(self):
        self.book_name = []
        self.book_status = []

    def display_welcome(self):
        print('Welcome to the library inventory! Here you will find all the books and their status.')
        pass

    def book_mode(self): 
        print('Would you like to add a book or see current available books?')
        user_input = input('Please enter 1 for adding new books or 2 to see current books: ')
        if user_input == '1' or user_input == '2':
            if user_input == '1':
                book_title = Books(input('Please enter book title: '))
                self.book_name.append(book_title)
                print('Book successfully added!')
            elif user_input == '2':
                if len(self.book_name) == 0:
                    print('There are currently no books in the inventory. Would you like to add one? ')
                    user_input = input('Please enter 1 for yes or 2 for no: ')
                    if user_input == '1' or user_input == '2':
                        if user_input == '1':
                            self.book_name = Books(input('Please enter book title: '))
                            print('Book successfully added!')
                        elif user_input == '2':
                            print('Okay, have a nice day!')
                    else:
                        print('Invalid option. Try again.')
                        self.book_mode()
        else:
            print('Invalid option. Try again')
            self.book_mode()
        pass

    def current_inventory(self):
        print('Current books in the inventory: ')
        for book in range(len(self.book_name)):
            print[book]

    def run_inventory(self):
        self.display_welcome()
        self.book_mode()
        self.current_inventory()
        pass