from Catalog import Catalog
from fine import fine
from BookItem import BookItem
class Issuer:
    def reserveBook(name, student_id, book_title, days):
        for book in Catalog.books:
            if book.title == book_title and len(book.book_item) != 0:
                book_item = book.book_item.pop()
                book.total_count -= 1
                Catalog.updateIssuer(book_item, name, student_id, days)
                Catalog.addToReservedList(book_item)
                return book_item
        else:
            print("The book you're trying to reserve is unavailable.")

    def returnBook(ret_book_item,days):
        if ret_book_item in BookItem.reserved_book_item:
            return ret_book_item
        BookItem.reserved_book_item.remove(ret_book_item)
        fine.calcBill(days)

    def extendDates(book_item, ext_days):
        Catalog.extendDates(book_item, ext_days)

