
class Book:
    def __init__(self, book_name):
        self.book_name = book_name
        self.book_status = 2
        pass

    def update_book_status(self):
        user_input = int(input(f'\nUpdating {self.book_name}\'s status. Please enter 1 for \'Checked Out\' or 2 for \'On Shelf\' status. Default is \'On Shelf\': '))
        if user_input == 1 or user_input == 2:
            if user_input == 1:
                self.book_status -= 1
                print(f'Updated {self.book_name}\'s to Checked Out!' )  
                return(self.book_status) 
            elif user_input == 2:
                print(f'Kept {self.book_name}\'s book status to On Shelf!')
        else:
            print('Invalid option. Please try again.')
            self.update_book_status()
        pass
