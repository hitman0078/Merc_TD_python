class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_details(self):
        return f"Name = {self.name}, Emp_id = {self.emp_id}"


employees = []   # store all employee objects here


def add_employee():
    name = input("Enter employee name: ")

    emp_id = input("Enter employee ID: ")

    # emp_id must be number
    if not emp_id.isdigit():
        print("Emp_id must be a number.")
        return

    emp_id = int(emp_id)

    # check if emp_id already exists
    for emp in employees:
        if emp.emp_id == emp_id:
            print("Emp_id ALREADY exists! Please use a unique ID.")
            return

    # otherwise create employee
    new_emp = Employee(name, emp_id)
    employees.append(new_emp)
    print("Employee ADDED successfully!\n")


# Add 2 employees
add_employee()
add_employee()

# Print all employees
print("\nAll employees:")
for e in employees:
    print(e.show_details())
