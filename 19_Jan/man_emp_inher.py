class Employee:
    def __init__(self, id, name, salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def get_id(self):
        return f"The ID is {self.__id}"

    def show_details(self):
        print(self.__id, self.__name, self.__salary)


class Manager(Employee):

    def __init__(self, id, name, salary, no_of_teams):
        super().__init__(id, name, salary)
        self.__no_of_teams = no_of_teams

    def show_details(self):
        super().show_details()
        print(self.__no_of_teams)


# Create objects and test
emp = Employee(1001, "xyz", 232323233)
emp.show_details()
mgr = Manager(101, "abc", 232323233, 5)
mgr.show_details()