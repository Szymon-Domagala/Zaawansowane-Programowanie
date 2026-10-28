from classes.zad_1 import Student
from classes.zad_2 import Employee
from typing import List


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
