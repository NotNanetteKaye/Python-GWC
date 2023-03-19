
class Library_Inventory:
    def __init__(self, inventory_name):
        self.inventory_name = inventory_name
        self.books = []
        pass

    def append_book_to_inventory(self, book):
        self.books.append(book)
        pass

    def loop_through_inventory(self):
        for i in range(len(self.books)):
            print('Book Name: ', self.books[i].book_name)
            if self.books[i].book_status == 1:
                print('Book Status: checked out')
            else:
                print('Book Status: on shelf')

    