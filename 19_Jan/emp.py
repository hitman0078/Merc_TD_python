class employee:
    def __init__(self, name=None, emp_id=None):
        self.name = name
        self.emp_id = emp_id
        
    def show_details(self):
        return f"The employee details are : name= {self.name}, emp_id= {self.emp_id}"
    
    def to_dict(self):
        return{'Name': self.name,'Emp_id': self.emp_id}
        
emp1 =  employee("Tara")
print(emp1.show_details())

emp2 = employee("Vedant", 232)
print(emp2.show_details())

emps= [emp1,emp2]
emps.append(employee())

for item in emps:
    print(item.show_details())
