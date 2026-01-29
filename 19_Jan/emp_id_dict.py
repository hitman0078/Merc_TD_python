class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        
    def to_dict(self):
        return {"name": self.name, "emp_id": self.emp_id}

    def show_details(self):
        return f"name = {self.name}, emp_id = {self.emp_id}"


# Store employees in a dict keyed by emp_id
employees_by_id = {}   # { emp_id (int): Employee }


def add_employee():
    name = input("Enter employee name: ").strip()
    emp_id_text = input("Enter employee ID (number): ").strip()

    if not emp_id_text.isdigit():
        print("Emp_id must be a positive number.")
        return

    emp_id = int(emp_id_text)

    # Check uniqueness using dict key
    if emp_id in employees_by_id:
        print(f"\nEmp_id: {emp_id} ALREADY EXISTS for: {employees_by_id[emp_id].name}.")
        return

    # Create and store employee
    emp = Employee(name, emp_id)
    employees_by_id[emp_id] = emp
    print("Employee ADDED successfully!")


add_employee()
add_employee()
            
print("\nAll employees:")
for eid, emp in employees_by_id.items():
    print(f"{eid} -> {emp.show_details()}")