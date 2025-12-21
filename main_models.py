from models.student import Student
from models.library import Library
from models.employee import Employee
from models.book import Book
from models.order import Order

# Biblioteki
library1 = Library("Krakow", "Basztowa", "30-001", "8-16", "123456789")
library2 = Library("Krakow", "Grodzka", "30-002", "9-17", "987654321")

# Pracownicy
emp1 = Employee("Jan", "Kowalski", "2020-01-01", "1990-05-10",
                "Krakow", "Basztowa", "30-001", "111111111")
emp2 = Employee("Anna", "Nowak", "2019-03-01", "1988-07-15",
                "Krakow", "Grodzka", "30-002", "222222222")

# Studenci
student1 = Student("Adam", 75)
student2 = Student("Katarzyna", 45)

# Książki
book1 = Book(library1, "2010", "Marta", "Kisiel", 328)
book2 = Book(library1, "2005", "Donna", "Tart", 450)
book3 = Book(library2, "2018", "Andrzej", "Sapkowski", 300)

# Zamówienia
order1 = Order(emp1, student1, [book1, book2], "2024-01-10")
order2 = Order(emp2, student2, [book3], "2024-01-12")

print(order1)
print("-" * 40)
print(order2)
