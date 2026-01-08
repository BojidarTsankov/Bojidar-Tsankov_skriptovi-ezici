class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        self.display()
        print(f"Section: {self.section}")


student1 = Student("Ivan Ivanov", 23, "Networking")
student1.displayStudent()
