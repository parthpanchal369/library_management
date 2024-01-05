class Library:

    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = {'Title:': title, 'Author':author, 'Available': True}
            print(f"Book '{title}' by '{author}' added to the library:")

        else:
            print("Book with the same ID already exists.")

    def display_book(self):
        print('\nLibrary Books:')
        for book_id, book_info in self.books.items():
            print(f"ID: {book_id}, Title: {book_info['title']}")

