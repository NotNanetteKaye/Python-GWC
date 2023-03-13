from library_inventory import Library_Inventory
from books import Books
from book_status import Book_Status



book1 = Library_Inventory()
dr_seuss = Books()
dr_seuss.book_name = 'dr.seuss'
checked_out = Book_Status()
checked_out.book_status = 'checked out'

book1.book_name.append(dr_seuss)
book1.book_status.append(checked_out)

print(book1.book_name[0].book_name)
print(book1.book_status[0].book_status)


# book1.run_inventory()
