# Book Management System

This Python program manages a collection of books, allowing users to add, delete, search, and update book records. It maintains a list of available books and a dictionary with detailed information about each book.

## Data Structures

### BooksAvailable
A dictionary containing detailed information about each book.

```python
BooksAvailable = {
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
```
```python
ListOfBooks = [
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
```
## addBook
Prompts the user to input details for a new book and adds it to the `BooksAvailable` dictionary and `ListOfBooks`.
```python
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
```
## removeBook
Removes a book from `BooksAvailable` and `ListOfBooks` using its Name & ISBN number.
``` python
def removeBook(self):
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
```
## searchBook
Searches for a book by its name in `ListOfBooks`.
``` python
def searchBooks(self):
        print("Enter the name of the book: ")
        bookName = input()
        if bookName in self.ListOfBooks:
            self.sleep
            print(f"{bookName} found!")
        else:
            print(f'No book named {bookName} found!')
```
## displayBooks
Displays all books available in `BooksAvailable` and `ListOfBooks`.
``` python
def displayBooks(self):
        for index, book in enumerate(self.ListOfBooks, 1):
            self.sleep
            print(f"{index}. {book}")
```
## updateBooks
Updates the details of a book in `BooksAvailable`.
``` python
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
```
# Usage
**Adding a Book:** Call the addBook() function and input the required details.

**Deleting a Book:** Call the deleteBook(books, isbn) function with the BooksAvailable dictionary and the ISBN of the book to be removed.

**Searching for a Book:** Call the searchBook(bookName) function with the name of the book.
Showing All Books: Call the showBooks() function.

**Updating a Book:** Call the updateBooks() function and input the new details of the book.

# Notes
  - The `isbn` input in `addBook()` and `updateBooks( )` functions should be a 14-digit number.
  - The functions assume that user inputs are correctly formatted.
  - The current implementation of `addBook()` and `updateBooks()` functions might not be correct as `BooksAvailable.update()` directly modifies the dictionary. This can be improved by using nested dictionaries for book details.

# Improvements
- Handle cases where the ISBN or book name already exists in `BooksAvailable`.
- Add validation for user inputs.
- Improve the `updateBooks()` function to correctly update existing book entries.