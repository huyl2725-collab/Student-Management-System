# Student model
class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.student_id} - {self.name} - {self.age}")