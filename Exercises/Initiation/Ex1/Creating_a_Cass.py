
#class structure for the Book.
class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def get_info(self):


        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}"

# Create an instance of the Book class
book = Book("Python Programming", "John Doe", 2021, "978-1234567890")


# Print the book's information using the get_info method
print(book.get_info())



