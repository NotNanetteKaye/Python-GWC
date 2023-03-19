
class Book:
    def __init__(self, book_name):
        self.book_name = book_name
        self.book_status = 2         # 2 sets default status of book to 'On Shelf'
        pass

    def update_book_status(self):
        user_input = input(f'\nUpdating {self.book_name}\'s status. Please enter 1 for \'Checked Out\' or 2 for \'On Shelf\' status. Default is \'On Shelf\': ')
        if user_input == '1' or user_input == '2':
            user_input = int(user_input)
            if user_input == 1:
                self.book_status -= 1
                print(f'Updated {self.book_name}\'s to Checked Out!' )  
                return(self.book_status) 
            elif user_input == 2:
                if self.book_status == 1:
                    self.book_status += 1
                    print(f'Updated {self.book_name}\'s book status to On Shelf!')
                else:
                    print(f'Kept {self.book_name}\'s status to On Shelf!')
        else:
            print('Invalid option. Please try again.')
            self.update_book_status()
        pass
