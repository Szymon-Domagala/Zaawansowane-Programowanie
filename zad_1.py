class Student:
    def __init__(self,name: str, marks: list):
        self.name = name
        self.marks = marks
    def is_passed(self) -> bool:
        sum = 0
        for mark in self.marks:
            sum += mark
        return (sum / len(self.marks)) > 5.0

if __name__ == "__main__":
    good_student = Student("Szymon", [5,6,6,5,6])
    bad_student = Student("Maksymilian", [2,2,2,2,2])
    student_list= [good_student,bad_student]

    for student in student_list:
        if student.is_passed():
            print("Ma średnią powyżej 5.0")
        else:
            print("Ma średnią poniżej 5.0")