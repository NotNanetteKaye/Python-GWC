from books import Books


class Library_Inventory:
    def __init__(self):
        self.book_name = []
        self.book_status = []
    
    def loop_through_lists(self):
        print('\nCurrent library inventory: ')
        for i in range(len(self.book_name)):
            print(f'\nBook Name: {self.book_name[i].book_name}')
            try:
                print(f'Book Status: {self.book_status[i].book_status}\n\n')
            except:
                print(f'Book Status: {self.book_status[i]}\n\n')
        pass