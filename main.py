from classes.zad_1 import Student
from classes.zad_2 import (
    Book,
    Employee,
    Library,
    Order
)
from classes.zad_3 import (
    Flat,
    House,
    Property
)

print("============================ Zad 1 ============================")
good_student = Student("Szymon", [5, 6, 6, 5, 6])
bad_student = Student("Maksymilian", [2, 2, 2, 2, 2])
student_list = [good_student, bad_student]

for student in student_list:
    if student.is_passed():
        print("Ma średnią powyżej 5.0")
    else:
        print("Ma średnią poniżej 5.0")

print("============================ Zad 2 ============================")
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

print("============================ Zad 3 ============================")
flat_1 = Flat(54.5, 3, 450000.0, "ul. Piotrkowska 12/4, Łódź", 2)
house_1 = House(120.0, 5, 850000.0, "ul. Słoneczna 15, Poznań", 600)

print(flat_1)
print("====================================================================")
print(house_1)
