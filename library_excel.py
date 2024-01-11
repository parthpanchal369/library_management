import pandas as pd


class Library:

    def __init__(self, excel_file="library_data.xlsx"):
        self.excel_file = excel_file
        self.books = self.load_data()

    def load_data(self):
        try:
            return pd.read_excel(self.excel_file, index_col=0).to_dict(orient='index')
        except FileNotFoundError:
            return {}

    def save_data(self):
        df = pd.DataFrame.from_dict(self.books, orient='index')
        df.to_excel(self.excel_file)
        print(f"Data saved to {self.excel_file}.")

    def add_book(self, title, author):
        book_id = len(self.books) + 1
        self.books[book_id] = {'title': title, 'author': author, 'available': True}
        self.save_data()
        print(f"Book '{title}' by {author} added to the library with ID: {book_id}.")

    def display_books(self):
        print("\nLibrary Books:")
        for book_id, book_info in self.books.items():
            print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Available: {book_info['available']}")

    def borrow_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id]['available']:
                self.books[book_id]['available'] = False
                self.save_data()
                print(f"Book '{self.books[book_id]['title']}' borrowed successfully.")
            else:
                print("Book is not available for borrowing.")
        else:
            print("Book with the given ID is not available.")

    def return_book(self, book_id):
        if book_id in self.books:
            if not self.books[book_id]['available']:
                self.books[book_id]['available'] = True
                self.save_data()
                print(f"Book '{self.books[book_id]['title']}' returned successfully.")
            else:
                print("Book is already available.")
        else:
            print("Book with the given ID does not exist.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice from 1-5: ")

        if choice == '1':
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.add_book(title, author)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            book_id = input("Enter Book ID to borrow: ")
            library.borrow_book(book_id)

        elif choice == '4':
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == '5':
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 to 5.")


if __name__ == '__main__':
    main()
