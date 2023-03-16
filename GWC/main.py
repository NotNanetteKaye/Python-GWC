from library_inventory import Library_Inventory
from books import Books
from book_status import Book_Status

inventory1 = Library_Inventory()
inventory1.inventory_name = 'Nanette Kaye'

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

inventory1.loop_through_lists()
