R_BONUS = 10000
DESIGNER_BONUS = 5000


class Employee:
    """
    Docstring for Employee
    """
    def __init__(self, name: str, salary: int):
        """
        Initializes a new Employee object.

        Args:
            name (str): The name of the employee.
            salary (int): The base annual salary of the employee.
        """
        self.name = name
        self.salary = salary

    def hello(self):
        """
        Prints a greeting message, identifying the class it's called from.
        """
        print(f"Hello from {self.__class__.__name__} Designer")

    def get_details(self) -> str:
        """
        Returns employee's name and base salary.

        Returns:
            str: A string describing the employee's name and salary.
        """
        return f"Employee Name: {self.name}, Salary: {self.salary}"


class Coder(Employee):
    """
    Represents a coder employee, inheriting from Employee.

    Coders have an additional attribute for their primary programming language
    and receive a specific bonus when their details are displayed.

    Attributes:
        name (str): The name of the coder.
        salary (int): The base annual salary of the coder.
        programming_language (str): Description
    """

    def __init__(self, name: str, salary: int, programming_language: str):
        """
        Initializes a new Coder object.

        Args:
            name (str): The name of the coder.
            salary (int): The base annual salary of the coder.
            programming_language (str): Description
        """
        super().__init__(name, salary)
        self.programming_language = programming_language

    def hello(self):
        """
        Prints a greeting message, identifying the class it's called from.
        """
        print(f"Hello from {self.__class__.__name__} Designer")

    def get_details(self) -> str:
        """
        Returns a formatted string containing the coder's name,
        salary (including a bonus), and programming language.

        Note: The bonus is applied for display purposes only and does not
        permanently modify the `self.salary` attribute.

        Returns:
            str: A string describing the coder's details.
        """
        bonus_salary = self.salary + CODER_BONUS
        return (f"Employee Name: {self.name}, Salary: {bonus_salary}, "
                f"Programming Language: {self.programming_language}")


class Designer(Employee):
    """
    Represents a designer employee, inheriting from Employee.

    Designers have an additional attribute for their primary design tool
    and receive a specific bonus when their details are displayed.

    Attributes:
        name (str): The name of the designer.
        salary (int): The base annual salary of the designer.
        design_tool (str): The primary design tool used by the designer.
    """

    def __init__(self, name: str, salary: int, design_tool: str):
        """
        Initializes a new Designer object.

        Args:
            name (str): The name of the designer.
            salary (int): The base annual salary of the designer.
            design_tool (str): The primary design tool used by the designer.
        """
        super().__init__(name, salary)
        self.design_tool = design_tool

    def hello(self):
        """
        Prints a greeting message, identifying the class it's called from.
        """
        print(f"Hello from {self.__class__.__name__} Designer")

    def get_details(self) -> str:
        """
        Returns a formatted string containing the designer's name,
        salary (including a bonus), and design tool.

        Note: The bonus is applied for display purposes only and does not
        permanently modify the `self.salary` attribute.

        Returns:
            str: A string describing the designer's details.
        """
        bonus_salary = self.salary + DESIGNER_BONUS
        return (f"Employee Name: {self.name}, Salary: {bonus_salary}, "
                f"Design Tool: {self.design_tool}")


if __name__ == "__main__":
    employees = [
        Employee("Alice", 70000),
        Coder("Bob", 90000, "Python"),
        Designer("Charlie", 80000, "Photoshop")
    ]

    for emp in employees:
        print(emp.get_details())