from library_inventory import Library_Inventory
from books import Books
from book_status import Book_Status

inventory1 = Library_Inventory()

book0 = Books()
book0.book_name = 'Dr. Seuss'
book0_status = Book_Status()
book0_status.book_status = 'checked out'
inventory1.book_name.append(book0)
inventory1.book_status.append(book0_status)

book1 = Books()
book1.book_name = 'Junie B. Jones'
book1_status = Book_Status()
inventory1.book_name.append(book1)
inventory1.book_status.append(book1_status.book_status)
# print(inventory1.book_status[1])

for i in range(len(inventory1.book_name)):
    print(f'Book Name: {inventory1.book_name[i].book_name}')
    try:
        print(f'Book Status: {inventory1.book_status[i].book_status}')
    except:
        print(f'Book Status: {inventory1.book_status[i]}')

# this can also work as well: inventory1.book_status[1] = 'checked out'
inventory1.book_status[1] = book1_status.update_book_status()

for i in range(len(inventory1.book_name)):
    print(f'Book Name: {inventory1.book_name[i].book_name}')
    try:
        print(f'Book Status: {inventory1.book_status[i].book_status}')
    except:
        print(f'Book Status: {inventory1.book_status[i]}')

# book1.run_inventory()
