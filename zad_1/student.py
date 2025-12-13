class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # lista ocen

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50
student1 = Student("Adam", [60, 70, 80])
student2 = Student("Katarzyna", [30, 40, 45])

print(student1.is_passed())  # True
print(student2.is_passed())  # False
