from BookItem import BookItem
class Book:
    def __init__(self,title,author,category,publish_date):
        self.title=title
        self.author=author
        self.publish_date=publish_date
        self.category=category
        self.total_count=0
        self.book_item=[]

    def addBookItem(self,isbn,rack):
        b=BookItem(self,isbn,rack)
        self.book_item.append(b)
        self.total_count+=1

    def printBook(self):
        print(self.title,self.author)
        for book_item in self.book_item:
            print(book_item.isbn,book_item.rack)

    def viewReservedBookItems():
        if len(BookItem.reserved_book_item) >= 1:
            for item in BookItem.reserved_book_item:
                print(item.isbn)
        else:
            print("No books are reserved at the moment!")

    def viewIssuer(isbn):
        for book_item in BookItem.reserved_book_item:
            if book_item.isbn == isbn:
                print("Issued by: " + book_item.info["Name"])
                print("Student ID: " + book_item.info["Student ID"])
                print("Issued for: " + str(book_item.info["Days"]) + " days")

    def updateIssuer(book_item, name, student_id, days):
        BookItem.updateIssuer(book_item, name, student_id, days)

    def addToReservedList(book_item):
        BookItem.addToReservedList(book_item)
    def extendDates(book_item, ext_days):
        BookItem.extendDates(book_item, ext_days)
    def __repr__(self):
        return self.name+' '+self.author