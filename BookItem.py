class BookItem:

    reserved_book_item=[]
    @classmethod

    def addReservedBooks(cls, book):
        cls.reserved_book_item.append(book)
    def __init__(self,book,isbn,rack):
        self.book = book
        self.isbn = isbn
        self.rack = rack
        self.info={}

    def updateIssuer(self,name,student_id,days):
        self.info['Name']=name
        self.info['studen Id']=student_id
        self.info['Days']=days

    def addToReservedList(self):
        BookItem.addReservedBooks(self)
    def extendDates(self, ext_days):
        if self.info["Days"] + ext_days <= 10:
            self.info["Days"] = self.info["Days"] + ext_days
            print("{} days extended successfully for {}".format(ext_days, self.isbn))
        else:
            print("Days cannot be extended over allowed maximum days.")