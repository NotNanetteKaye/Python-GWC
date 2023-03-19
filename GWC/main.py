from library_inventory import Library_Inventory
from books import Books
from book_status import Book_Status

inventory1 = Library_Inventory()
inventory1.inventory_name = 'Nanette'

book0 = Books('Dr. Seuss')
print(book0.book_status)