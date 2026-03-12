import streamlit as st

# Parent Class
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def details(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.is_available}"


# Child Class
class LibraryBook(Book):

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"{self.title} borrowed successfully."
        else:
            return f"{self.title} is not available."

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"{self.title} returned successfully."
        else:
            return f"{self.title} was not borrowed."


# Library Manager
class Library:

    def __init__(self):
        self.books = []
        self.book_counter = 1

    def add_book(self, title, author):
        book = LibraryBook(self.book_counter, title, author)
        self.books.append(book)
        self.book_counter += 1
        return f"Book '{title}' added successfully."


library = Library()

st.title("📚 Library Management System")

title = st.text_input("Enter Book Title")
author = st.text_input("Enter Author Name")

if st.button("Add Book"):
    st.success(library.add_book(title, author))

if st.button("Show Available Books"):
    st.subheader("Available Books")
    for book in library.books:
        if book.is_available:
            st.write(book.details())
            