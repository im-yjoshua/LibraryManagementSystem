import time

class LibraryManagementSystem:
    def __init__(self):
        self.sleep = time.sleep(1)
        self.BooksAvailable = {
            "To Kill a Mockingbird": {
                "author": "Harper Lee",
                "price_usd": 7.99,
                "isbn": "9780061120084",
                "genre": "Fiction"
            },
            "1984": {
                "author": "George Orwell",
                "price_usd": 9.99,
                "isbn": "9780452284234",
                "genre": "Dystopian, Political Fiction"
            },
            "The Great Gatsby": {
                "author": "F. Scott Fitzgerald",
                "price_usd": 10.99,
                "isbn": "9780743273565",
                "genre": "Tragedy"
            },
            "Harry Potter and the Sorcerer's Stone": {
                "author": "J.K. Rowling",
                "price_usd": 8.99,
                "isbn": "9780590353403",
                "genre": "Fantasy"
            },
            "The Catcher in the Rye": {
                "author": "J.D. Salinger",
                "price_usd": 6.99,
                "isbn": "9780316769480",
                "genre": "Realistic Fiction"
            },
            "The Lord of the Rings: The Fellowship of the Ring": {
                "author": "J.R.R. Tolkien",
                "price_usd": 13.99,
                "isbn": "9780618002228",
                "genre": "Fantasy"
            },
            "Pride and Prejudice": {
                "author": "Jane Austen",
                "price_usd": 5.99,
                "isbn": "9780199535569",
                "genre": "Romance"
            },
            "The Hobbit": {
                "author": "J.R.R. Tolkien",
                "price_usd": 8.99,
                "isbn": "9780618002211",
                "genre": "Fantasy"
            },
            "Fahrenheit 451": {
                "author": "Ray Bradbury",
                "price_usd": 7.99,
                "isbn": "9780743247222",
                "genre": "Dystopian"
            },
            "Jane Eyre": {
                "author": "Charlotte Brontë",
                "price_usd": 6.99,
                "isbn": "9780141441146",
                "genre": "Romance"
            }
        }
        self.ListOfBooks = [
            "To Kill a Mockingbird",
            "1984",
            "The Great Gatsby",
            "Harry Potter and the Sorcerer's Stone",
            "The Catcher in the Rye",
            "The Lord of the Rings: The Fellowship of the Ring",
            "Pride and Prejudice",
            "The Hobbit",
            "Fahrenheit 451",
            "Jane Eyre"
        ]

        while True:
            print("\nWelcome to the Library Management System")
            self.sleep
            print("1. Add a Book")
            print("2. Remove a Book")
            print("3. Search for a Book")
            print("4. Display All Books")
            print("5. Update Book Information")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.addBook()
            elif choice == "2":
                self.removeBook()
            elif choice == "3":
                self.searchBooks()
            elif choice == "4":
                self.displayBooks()
            elif choice == "5":
                self.updateBook()
            elif choice == "6":
                print("Exiting System.....")
                time.sleep(1)
                break
            else:
                print("Invalid Choice")

    def addBook(self):
        print("Enter the name of the book:")
        bookName = input()
        print("Enter the name of the author:")
        authorName = input()
        print("Enter the price of the book:")
        bookPrice = input()
        print("Enter the ISBN of the book:")
        bookISBN = input()
        print("Enter the genre of the book:")
        bookGenre = input()
        self.BooksAvailable.update({
            bookName: {
                "author": authorName,
                "price_usd": bookPrice,
                "isbn": bookISBN,
                "genre": bookGenre
            }
        })
        self.ListOfBooks.append(bookName)
        self.sleep
        print(f"{bookName} with ISBN {bookISBN} added Successfully!")

    def removeBook(self,):
        print("Enter the name of the book:")
        bookName = input()
        print("Enter the ISBN of the book:")
        bookISBN = input()

        book_to_remove = None
        for book, details in self.BooksAvailable.items():
            if details["isbn"] == bookISBN:
                book_to_remove = book
                break

        if book_to_remove:
            del self.BooksAvailable[book_to_remove]
            self.sleep
            print(f"{bookName} with ISBN {bookISBN} removed successfully!")
        else:
            self.sleep
            print(f"No book found with ISBN: {bookISBN}")

        for book in self.ListOfBooks:
            if book == bookName:
                self.ListOfBooks.remove(bookName)
                break

    def searchBooks(self):
        print("Enter the name of the book: ")
        bookName = input()
        if bookName in self.ListOfBooks:
            self.sleep
            print(f"{bookName} found!")
        else:
            print(f'No book named {bookName} found!')

    def displayBooks(self):
        for index, book in enumerate(self.ListOfBooks, 1):
            self.sleep
            print(f"{index}. {book}")

    def updateBook(self):
        print("Enter the name of the book: ")
        bookName = input()
        print("Enter the ISBN of the book: ")
        bookISBN = input()
        print("Enter the name of the author: ")
        authorName = input()
        print("Enter the price of the book: ")
        bookPrice = input()
        print("Enter the genre of the book: ")
        bookGenre = input()
        
        self.BooksAvailable.update({
            bookName: {
                "author": authorName,
                "price_usd": bookPrice,
                "isbn": bookISBN,
                "genre": bookGenre
            }
        })
        self.ListOfBooks.append(bookName)
        self.sleep
        print(f"{bookName} with ISBN {bookISBN} successfully updated!")


if __name__ == "__main__":
    system = LibraryManagementSystem()
    print(system)
