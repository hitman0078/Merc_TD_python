from abc import ABC, abstractmethod


class Person(ABC):

    """Person class"""
    @abstractmethod
    def do_something(self):  # only declaration no body

        """Do something"""


class Student(Person):

    """Student class inheriting from person"""
    def do_something(self):

        """Do something (Polymorphism)"""
        print("Student is studying.")


class Employee(Person):

    """Employee class"""
    def do_something(self):

        """Do something (polymorphism) from person class"""
        print("Employee is working.")


# p1=Person();
p1 = Student()
p1.do_something()
p2 = Employee()
p2.do_something()