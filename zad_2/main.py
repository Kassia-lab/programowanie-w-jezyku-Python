from student import Student
from library import Library
from employee import Employee
from book import Book
from order import Order

# Biblioteki
library1 = Library("Warsaw", "Main St", "00-001", "8-16", "123456789")
library2 = Library("Krakow", "Old Town", "30-002", "9-17", "987654321")

# Pracownicy
emp1 = Employee("Jan", "Kowalski", "2020-01-01", "1990-05-10",
                "Warsaw", "Main St", "00-001", "111111111")
emp2 = Employee("Anna", "Nowak", "2019-03-01", "1988-07-15",
                "Krakow", "Old Town", "30-002", "222222222")
emp3 = Employee("Piotr", "Nowakowski", "2021-06-01", "1995-02-20",
                "Warsaw", "Side St", "00-003", "333333333")

# Studenci
student1 = Student("Adam")
student2 = Student("Katarzyna")
student3 = Student("Marek")

# Książki
book1 = Book(library1, "2010", "Marta", "Kisiel", 328)
book2 = Book(library1, "2005", "Donna", "Tart", 450)
book3 = Book(library2, "2018", "Andrzej", "Sapkowski", 300)
book4 = Book(library2, "2020", "Stephen", "King", 520)
book5 = Book(library1, "1999", "Dan", "Brown", 410)

# Zamówienia
order1 = Order(emp1, student1, [book1, book2], "2024-01-10")
order2 = Order(emp2, student2, [book3, book4, book5], "2024-01-12")

# Wyświetlenie zamówień
print(order1)
print("-" * 40)
print(order2)
