# Library Management System
# Objective: Create a simple Library Management System where users can manage a collection
# of books. This project will involve using lists, tuples, dictionaries, and functions to perform
# various operations like adding, removing, searching, and displaying books.
# Functional Requirements:
# 1. Add a Book:
# ○ Users should be able to add a book to the library.
# ○ Each book can be represented as a dictionary with keys like title, author,
# year_published, and isbn.
# ○ Store all books in a list.
# 2. Remove a Book:
# ○ Users should be able to remove a book using its isbn.
# 3. Search for a Book:
# ○ Users should be able to search for books by title or author.
# ○ Display the details of the matching books.
# 4. Display All Books:
# ○ Display a list of all the books currently in the library, showing their details.
# 5. Update Book Information:
# ○ Users should be able to update the details of an existing book using its isbn.
# Project Outline:
# 1. Main Menu:
# ○ Display options for the user to choose from:
# ■ Add a Book
# ■ Remove a Book
# ■ Search for a Book
# ■ Display All Books
# ■ Update Book Information
# ■ Exit
# 2. Functions:
# ○ add_book(library): Prompts the user for book details and adds the book to the
# library.
# ○ remove_book(library): Prompts the user for an isbn and removes the
# corresponding book.
# ○ search_books(library): Prompts the user for a search term (either title or
# author) and displays matching books.
# ○ display_books(library): Displays all books in the library.
# ○ update_book(library): Prompts the user for an isbn and allows updating of
# book details.
# Data Structures:
# ● List: Used to store the collection of books.
# ● Dictionary: Used to represent each book with its details.
# Functions:
# ● Learn to write modular code by creating functions for each operation.
# ● Understand how to pass and manipulate data using function parameters.
# User Input:
# ● Practice handling user input and validating it.
# Conditional Statements:
# ● Use if-else statements to navigate the main menu and handle different user choice


# # ===================================

class LibraryManagementSystem:
    def __init__(self):
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
    pass

    def addBook(self):
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

        self.BooksAvailable.update({
            "author": authorName,
            "price_usd": bookPrice,
            "isbn": bookISBN,
            "genre": bookGenre})

        self.ListOfBooks.append(bookName)
        print(self.BooksAvailable)
        print(self.ListOfBooks)
        pass

if __name__ == "__main__":
    a = LibraryManagementSystem()
    print(a.addBook())
