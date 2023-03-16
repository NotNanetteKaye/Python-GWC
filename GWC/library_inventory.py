from books import Books


class Library_Inventory:
    def __init__(self):
        self.inventory_name = ''
        self.book_name = []
        self.book_status = []
    
    def loop_through_inventory_list(self):
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

    def update_inventory_book_status(self):
        user_input = int(input('Please enter 1 for checked out or 2 for on shelf status. Default is on shelf: '))
        if user_input == 1 or user_input == 2:
            if user_input == 1:
                self.book_status = self.book_status.replace('on shelf', 'checked out')
                print('Updated to checked out!' )
            elif user_input == 2:
                book_status = 'on shelf'
                print('Kept the status to on shelf!')
                return(book_status)
        else:
            print('Invalid option. Please try again.')
            self.update_book_status()
        pass