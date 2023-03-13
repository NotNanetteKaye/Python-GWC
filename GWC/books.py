class Books:
    def __init__(self):
        self.book_name = []
        self.book_status = 'on shelf'

    def update_book_status(self):
        user_input = int(input('Please enter 1 for checked out or 2 for on shelf status. Default is on shelf: '))
        if user_input == 1 or user_input == 2:
            if user_input == 1:
                self.book_status = 'checked out'
                print(f'Updated {self.book_name} to checked out!' )
            elif user_input == 2:
                print(f'{self.book_name} is on shelf!')
        else:
            print('Invalid option. Please try again.')
            self.update_book_status()
        pass