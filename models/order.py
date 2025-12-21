from models.book import Book
from models.employee import Employee
from models.student import Student


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = ", ".join(str(book) for book in self.books)
        return (
            f"Order date: {self.order_date}\n"
            f"{self.employee}\n"
            f"{self.student}\n"
            f"Books: {books_str}"
        )
