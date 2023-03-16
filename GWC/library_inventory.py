from books import Books


class Library_Inventory:
    def __init__(self):
        self.inventory_name = ''
        self.book_name = []
        self.book_status = []
    
    def loop_through_lists(self):
        print('\n- - - - - - - - - - - - - -\n')
        print(f'{self.inventory_name}\'s library inventory:\n')
        for i in range(len(self.book_name)):
            print(f'Book Name: {self.book_name[i].book_name}')
            try:
                print(f'Book Status: {self.book_status[i].book_status}\n')
            except:
                print(f'Book Status: {self.book_status[i]}\n')
        print('- - - - - - - - - - - - - -')
        pass