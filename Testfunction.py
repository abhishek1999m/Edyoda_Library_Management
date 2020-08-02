import sys
from Book import Book
from Catalog import Catalog
from User import  Librarian
from User import Member



m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')

lib = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101')
lib.addBook('Shoe Dog','Phil Knight',"Biography",'2015')
lib.addBookItem("Shoe Dog", "123pk", "H1B1")
lib.addBookItem("Shoe Dog", "124pk", "H1B2")
lib.addBook('Kafka On The Shore','Haruki Murakami', "Fiction",'2002')
lib.addBookItem("Kafka On The Shore", "854hm", "C1B1")
lib.addBookItem("Kafka On The Shore", "685hm", "C1B2")
lib.addBook('The Fault In Our Stars','John Green', "Romance",'2012')
lib.addBookItem("The Fault In Our Stars", "957jg", "R1B1")
lib.addBookItem("The Fault In Our Stars", "985jg", "R1B2")

b = lib.addBook('Moonwalking with Einstien','J Foer','Adventure','2017')
lib.addBookItem(b, '463hg','K1B2')

while (True):
    print("welocome to the {} library.please Enter your choice".format(lib.name))
    print("1", "display_books")
    print("2", "Issue_book")
    print("3", "Return book")
    print("4", "Search book By book_Name")
    print("5", "Search book By Author_Name")
    print("\n")
    print("this is Librarian task please login with Librarian_id to perform task")
    print("6","Search Member")
    print("7", "Add book")
    print("8", "Remove book")
    print("9", "Add Memeber")
    print("10", "Remove Member")
    print("11", "View Member")
    user_choice = input()
    if user_choice not in ["1", "2", "3", "4", "5", "6", "7", "8","9","10","11"]:
        print("please Enter correct choice \n")
        continue
    else:
        user_choice=int(user_choice)
        if user_choice==1:
            print("we have following books in {} library".format(lib.name))
            lib.viewBooks()
            print("\n")
        elif user_choice==2:
            book=input("Please Enter the Name of the book you want to isssue:")
            user=input("Please Enter your Name")
            m1.reserveBook(book)
            print("\n")

        elif user_choice==3:
            user = input("please enter your name:")
            m1.returnBook()
            print("\n")
        elif user_choice==4:
            title = input("Enter the name of book: ")
            Catalog.searchByTitle(title)
            print("\n")
        elif user_choice == 5:
            Author = input("Enter the name of author: ")
            Catalog.searchByAuthor(Author)
            print("\n")
        elif user_choice==6:
            name=input("Enter name of Member:")
            lib.searchMember(name)
        elif user_choice == 7:
            username = input("username: ")
            print(lib)
            print("now you can add book in library")
            print("\n")
            book_name = input("Enter the name of the book you want to add: ")
            quantity = int(input("Enter quantity of book to add: "))
            author = input("Enter the name of author: ")
            rack = input("Enter rack number: ")
            publish_date = input("Enter the publish_date: ")
            pages = input("Enter the total number of page of book: ")
            lib.addBook( book_name,author, publish_date, pages)
            lib.addBookItem(book_name,quantity,rack)
            print("\n")
        elif user_choice == 8:
            username = input("username: ")
            emp_id = input("password: ")
            libr = lib(username,"Bangalore",34,'asljlkj22',emp_id)
            print("now you can remove book from library")
            print("\n")
            book_name = input("Enter the name of the book you want to remove: ")
            rack = input("Enter rack number: ")
            lib.removeBookItem(book_name,rack)
            print("\n")
        elif user_choice==9:
            mem_name=input("Enter name of Member: ")
            location=input("Enter location Of Member: ")
            age=input("Enter age of Member: ")
            ad_id=input("Enter aadhar Id: ")
            st_id=input("Enter student Id")
            lib.Member(mem_name,location,age,ad_id,st_id)
            print("\n")
        elif user_choice==10:
            name=input("Enter the name of Member you want to remove: ")
            lib.removeMember(name)
            print("\n")
        elif user_choice==11:
            print("You are now going to see all the list of member: ")
            lib.viewMembers()
        else:
            print("Not a valid option")

        print("press q to quit or c to conitinue")
        choice = ""
        while (choice != "c" and choice != "q"):
            choice = input()
            if choice == "c":
                continue
            elif choice == "q":
                sys.exit()
