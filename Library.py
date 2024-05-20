class Library:
    def __init__(self,list):
        self.books_list = list
        self.available_books_list = list
        self.books_lent = {} #key-books
    def display_available_books(self):
        for i in self.available_books_list:
            print(i)

    def display_all_books(self):
        for i in self.books_list:
           print(i)

    def lend_book (self,name,book):
         if book not in self.books_list:
             print("Incorrect book name.please check in book list")
             return
         if book in self.available_books_list:
             self.books_lent.update({book:name})
             self.available_books_list.remove(book)
             print(" you can take the book ")
         else:
            print(" the book is allready taken " + book)
    def return_book(self,book):
        del self.books_lent[book]
        self.available_books_list.append(book)


if __name__=="__main__":
    lib = Library(["The life divine","da vince code","alchemist","The fish on tree"])
    print("Welcome to library.Enter an option")
    print("1.display the available books")
    print("2.display all books")
    print("3.Barrow a book")
    print("4.Return a book")
    print("5.Quit")
    while True:
        user_chioce = int(input())
        if user_chioce ==1:
            lib.display_available_books()
        elif user_chioce ==2:
            lib.display_all_books()
        elif user_chioce ==3:
            name = input("Enter User Name")
            book = input(" Enter the book name ")
            lib.lend_book(name,book)
        elif user_chioce ==4:
            book = input("Enter the name of the book")
            lib.return_book(book)
        elif user_chioce ==5:
            break
        else:
            print("invalid choice")






