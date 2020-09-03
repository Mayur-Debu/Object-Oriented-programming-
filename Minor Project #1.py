"""
MINOR PROJECT NO: 1
This minor project is a library management system based on object oriented programming concepts.
"""

class Library(object):
    bookDictionary={}
    books=["C Programming","C++ Programming","Java Programming","Python Programming","Javascript Programming"]

    def __init__(self,name):
        self.name=name

    @staticmethod
    def print_all_available_books():
        print("\nAvailable books are:",end="\n")
        for i in Library.books:
            print(i,end="\n")

    def issue_book(self,bookName):
        self.bookName=bookName
        if (self.bookName in self.books):
            self.bookDictionary.update({self.bookName:self.name})
            print(f"{self.bookName} is issued to {self.name}")
            self.books.remove(self.bookName)
        else:
            print("Your requested book is not available in library")
            print(f"That book {self.bookName} was issued to {self.bookDictionary.get(self.bookName)} ")

    def return_book(self,bookName):
        self.bookName=bookName
        if (self.bookName in self.books):
            print(f"You don't have that book. CALM DOWN !!!!")
        else:
            self.books.append(self.bookName)
            print("Book Returned Successfully. Thank you Visit Again!!!")

    def donate_book(self):
        donatedBook=input("Enter Book Name: ")
        self.donatedBook=donatedBook
        self.books.append(self.donatedBook)
        print(f"Thank you {self.name} for donating the book!!! We highly appreciate your gesture")





if __name__ == '__main__':

    print("**********WELCOME TO THE ONLINE LIBRARY MANAGEMENT SYSTEM**************")

    while(True):

        print("\n")
        print("1: Create New User.",end="\n")
        print("2: Print all Available Books.",end="\n")
        print("3: Issue a Book.",end="\n")
        print("4: Return a Book.",end="\n")
        print("5: Donate a Book.,",end="\n")
        print("6: To Quit The Library Management System",end='\n')
        choice=int(input("\nChoose a Option==>  "))

        if   choice ==  1:
            user=Library(input("Enter Name: "))
        if choice ==  2:
            Library.print_all_available_books()
        elif choice ==  3:
            user.issue_book(input("\nEnter Book Name: "))
        elif choice ==  4:
            user.return_book(input("\nEnter Book Name to Return: "))
        elif choice ==  5:
            user.donate_book()
            # pass
        elif choice ==  6:
            print("\nThank You!!! Please visit again.....")
            break
        else:
            print("\nINVALID CHOICE !!! KINDLY TRY AGAIN....")

