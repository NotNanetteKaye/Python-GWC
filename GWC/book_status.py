from library_inventory import Library_Inventory

class Book_Status(Library_Inventory):
    def __init__(self):
        super().__init__()
        self.book_status = []
        pass

    def update_book_status(self):
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

