from Book import Book
from BookItem import BookItem

class Catalog:
    different_book_count = 0
    books = []
    @classmethod
    def addBooksList(cls,book):
        cls.books.append(book)
    # Only available to admin
    def addBook(self,title, author, category, publication_date):
        b = Book(title, author, category, publication_date)
        Catalog.addBooksList(b)
        Catalog.different_book_count += 1
        print("Book {} has been added successfully!".format(title))
    # Only available to admin
    def addBookItem(title, isbn, rack):
        for book in Catalog.books:
            if book.title == title:
                b=Book.addBookItem(book,isbn, rack)
                print("Book{} has bee added successfully!".format(isbn))

    def removeBook(rem_book):
        for book in Catalog.books:
            if book.title == rem_book:
                Catalog.books.remove(book)
                Catalog.different_book_count -= 1
                print("Book {} has been removed from the catalog!".format(rem_book))

    def removeBookItem(rem_bookitem):
        for book in Catalog.books:
            for book_item in book.book_item:
                if book_item.isbn == rem_bookitem:
                    book.book_item.remove(book_item)
                    book.total_count -= 1
                    print("Book Item {} has been removed from the catalog!".format(rem_bookitem))

    def searchByTitle(title):
        for book in Catalog.books:
            if title.strip() == book.title:
                print("Book is available with this name:")
                return book
        else:
            print("Sorry.. no book is present of this titleand author!")


    def searchByAuthor(author):
        count=0
        for book in Catalog.books:
           if author.strip()==book.author:
                print(book.title)
                count+=1
        if count==0:
            print("Sorry.. no books are available by this author!")

    def displayAllBooks(self):
        print('Different Book Count', Catalog.different_book_count)
        c = 0
        for book in Catalog.books:
            c += book.total_count
            book.printBook()

        print('Total Book Count', c)

    def updateIssuer(book_item,name,student_id,days):
        Book.updateIssuer(book_item,name,student_id,days)

    def addToReservedList(book_item):
        Book.addToReservedList(book_item)

    def removeFromReservedList(ret_book_item):
        BookItem.removeFromReservedList(ret_book_item)

    def extendDates(book_item, ext_days):
        Book.extendDates(book_item, ext_days)

    def viewReservedBookItems():
        Book.viewReservedBookItems()

    def viewIssuer(isbn):
        Book.viewIssuer(isbn)