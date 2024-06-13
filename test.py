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


def addBook():
    print("Enter the name of the book:")
    bookName = input()
    print("Enter the name of the author:")
    authorName = input()
    print("Enter the price of the book: ")
    bookPrice = input()
    print("Enter the 14 digit ISBN number: ")
    bookISBN = int(input())
    print("Enter the genre of the book: ")
    bookGenre = input()

    BooksAvailable.update({
        "author": authorName,
        "price_usd": bookPrice,
        "isbn": bookISBN,
        "genre": bookGenre})

    ListOfBooks.append(bookName)
    print(BooksAvailable)
    print(ListOfBooks)


def deleteBook(books, isbn):
    # Find the key (book title) for the given ISBN
    book_to_remove = None
    for book, details in books.items():
        if details["isbn"] == isbn:
            book_to_remove = book
            break

    # If the book is found, remove it from the dictionary
    if book_to_remove:
        del books[book_to_remove]
    else:
        print(f"No book found with ISBN: {isbn}")
    pass


def searchBook(bookName):
    for book in ListOfBooks:
        if book == bookName:
            print(book)


def showBooks():
    for book in BooksAvailable:
        print(f"{book} ")


def updateBooks():
    print("Enter the name of the book:")
    bookName = input()
    print("Enter the name of the author:")
    authorName = input()
    print("Enter the price of the book: ")
    bookPrice = input()
    print("Enter the 14 digit ISBN number: ")
    bookISBN = int(input())
    print("Enter the genre of the book: ")
    bookGenre = input()

    BooksAvailable.update({
        "author": authorName,
        "price_usd": bookPrice,
        "isbn": bookISBN,
        "genre": bookGenre})

    ListOfBooks.append(bookName)
    print(BooksAvailable)
    print(ListOfBooks)