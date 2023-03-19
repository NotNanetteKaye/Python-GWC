from library_inventory import Library_Inventory
from books import Book

inventory0 = Library_Inventory('Nanette Kaye')

book0 = Book('Dr. Seuss')
inventory0.append_book_to_inventory(book0)

book1 = Book('Junie B. Jones')
inventory0.append_book_to_inventory(book1)

inventory0.loop_through_inventory()
book0.update_book_status()
inventory0.loop_through_inventory()


inventory1 = Library_Inventory('Autodesk') # Create multiple inventories 
inventory1.append_book_to_inventory(book0) # Append same book to multiple inventories
inventory1.loop_through_inventory() # Inventory 1 would carry the same book status from Inventory 0 of 'Checked Out'
