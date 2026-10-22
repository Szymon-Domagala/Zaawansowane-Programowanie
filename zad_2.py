from zad_1 import Student
from typing import List


class Library:
    def __init__(self, city: str, street: str, zip_code: str,
                 open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Adres biblioteki {self.zip_code} {self.city} ul. {self.street}"
            f"\nGodziny otwarcia {self.open_hours}"
            f"\nNumer kontaktowy {self.phone}"
            )


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str,
                 birth_date: str, city: str, street: str,
                 zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Pracownik {self.first_name} {self.last_name}"
            f"\nZatrudniony {self.hire_date}\nUrodzony {self.birth_date}"
            f"\nAdres zamieszkania {self.zip_code} {self.city} {self.street}"
            f"\nNumer kontaktowy {self.phone}"
            )


class Book:
    def __init__(self, library: Library, publication_date: str,
                 author_name: str, author_surname: str,
                 number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka pochodzi z biblioteki:\n{self.library}"
            f"\nData publikacji {self.publication_date}"
            f"\nAutor {self.author_name} {self.author_surname}"
            f"\nIlość stron {self.number_of_pages}"
        )


class Order:
    def __init__(self, employee: Employee, student: Student,
                 books: List[Book], order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n".join(f"- {book}" for book in self.books)
        return (
            f"Zamówienie obługiwane przez pracownika:\n{self.employee}"
            f"\nDla studenta {self.student.name}"
            f"\nZamówione ksiązki {books_str}"
            f"\nData zamówienia"
        )


library_1 = Library("Sosnowiec", "Kalinowa", "41-200", "8-16", "654 432 312")
library_2 = Library("Katowice", "Grunwaldzka", "43-212", "6-14", "142 213 213")

book_1 = Book(library_1, "12-08-2000", "Józef", "Kowalski", "561")
book_2 = Book(library_1, "04-02-2003", "Jakub", "Adamski", "741")
book_3 = Book(library_2, "11-10-1997", "Amelia", "Wybicka", "421")
book_4 = Book(library_2, "27-12-1999", "Wisława", "Nawrocka", "843")
book_5 = Book(library_2, "07-06-2005", "Zbigniew", "Tuck", "899")

employee_1 = Employee("Oliwier", "Nowacki", "24-10-2026", "01-05-2000",
                      "Katowice", "Wolności", "43-212", "564 312 212")
employee_2 = Employee("Julia", "Łęcka", "15-12-2019", "09-11-2003",
                      "Gliwice", "Dąbrowska", "46-321", "765 671 678")
employee_3 = Employee("Jakub", "Huczny", "04-02-2025", "01-01-2000",
                      "Sosnowiec", "Niwecka", "41-200", "788 432 231")

student_1 = Student("Szymon", [1, 2, 3, 4])
student_2 = Student("Jan", [5, 4, 2, 3])
student_3 = Student("Wojtek", [4, 5, 4])

order_1 = Order(employee_1, student_3, [book_1, book_2], "20-10-2026")
order_2 = Order(employee_2, student_2, [book_3, book_4, book_5], "10-10-2026")

print(order_1)
print("====================================================================")
print(order_2)
