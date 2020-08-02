from Issuer import Issuer
from Catalog import Catalog

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id

    def viewBooks(self):
        Catalog.displayAllBooks(self)

class Librarian(User):
    def __init__(self, name, location, age, aadhar_id, employee_id):
        super().__init__(name, location, age, aadhar_id)
        self.employee_id = employee_id

    def __repr__(self):
        return self.name + " " + self.location + " " + self.employee_id

    def addBook(self,title, author, category, publication_date):
        Catalog.addBook(self,title, author, category, publication_date)

    def addBookItem(self, title, isbn, rack):
        Catalog.addBookItem(title, isbn, rack)

    def removeBook(self, rem_book):
        Catalog.removeBook(rem_book)

    def removeBookItem(self, rem_bookitem):
        Catalog.removeBookItem(rem_bookitem)

    def addMember(self, name, location, age, aadhar_id, student_id):
        Member(name, location, age, aadhar_id, student_id)

    def removeMember(self, name):
        for member in Member.members_list:
            if member.name == name:
                Member.members_list.remove(member)
                print("{} was successfully removed from the library!".format(name))
                break
        else:
            print("No member exists by this name")

    def viewMembers(self):
        for member in Member.members_list:
            print(member)

    def searchMember(self, name):
        for member in Member.members_list:
            if member.name == name:
                print(member)
                for book_item in member.issued_books_list:
                    print(book_item.book.title, book_item.isbn)
                break
        else:
            print("There are no registered members in this library by this name.")

    def viewReservedBookItems(self):
        Catalog.viewReservedBookItems()

    def viewIssuer(self):
        isbn = input("Please enter isbn of the book for which you'd like to view issuer information for: ")
        Catalog.viewIssuer(isbn)

class Member(User):
    members_list = []

    @classmethod
    def addMemberList(cls, member):
        cls.members_list.append(member)

    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issued_books_list = []
        Member.addMemberList(self)
        print("Welcome to  Members Library {}!".format(name))

    def __repr__(self):
        return self.name + " " + self.location + " " + self.student_id

    def searchByTitle(self, title):
        Catalog.searchByTitle(title)

    def searchByAuthor(self, author):
        Catalog.searchByAuthor(author)

    def reserveBook(self, book_title):
        days = 0
        max_days = 10
        for member in Member.members_list:
            if member == self:
                days = int(input("For how many days would you like to issue this book? "))

        if days <= max_days:
            if len(member.issued_books_list)<5:
                print("You can Issue Book till",days," Days")
                book_item = Issuer.reserveBook(self.name, self.student_id, book_title, days)
                self.issued_books_list.append(book_item)
            else:
                print("Sorry! You can only issue 5 Books at a time:")
        else:
            print("Sorry! Max no.of days for issued book is 10 Days!")
    def returnBook(self):
        print("BOOKS CURRENTLY ISSUED BY YOU: ")
        book = input("Which book would you like to return? Enter isbn: ")
        days = int(input("How many days has it been since you issued this book? Be honest! "))
        Issuer.returnBook(book,days)
        self.issued_books_list.remove(book)

    def extendDates(self):
        print("BOOKS CURRENTLY ISSUED BY YOU: ")
        for book_item in self.issued_books_list:
            print(book_item.isbn)
        isbn = input("Please enter isbn of the book for which you'd like to extend dates: ")
        ext_days = int(input("Please enter the number of days you'd like to extend for: "))
        for book_item in self.issued_books_list:
            if book_item.isbn == isbn:
                Issuer.extendDates(book_item, ext_days)