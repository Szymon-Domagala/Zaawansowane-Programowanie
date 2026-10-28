class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        sum = 0
        for mark in self.marks:
            sum += mark
        return (sum / len(self.marks)) > 5.0
