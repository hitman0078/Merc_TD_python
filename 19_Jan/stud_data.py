from typing import List, Optional
 
class Student:
    def __init__(self, id: int, name: str, total_marks: float):
        self.id = id
        self.name = name
        self.total_marks = total_marks
 
    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}', marks={self.total_marks})"
 
 
class Teacher:
    def __init__(self, id: int, name: str, student_list: Optional[List[Student]] = None):
        self.id = id
        self.name = name
        self.student_list = student_list if student_list is not None else []
 
    # Add student
    def add_student(self, student: Student) -> None:
        if any(s.id == student.id for s in self.student_list):
            raise ValueError(f"Student with id {student.id} already exists")
        self.student_list.append(student)
 
    # 1. Total strength
    def total_strength(self) -> int:
        return len(self.student_list)
 
    # 2. Display students in descending order of marks
    def display_descending(self) -> None:
        if not self.student_list:
            print("No students available")
            return
 
        sorted_students = sorted(
            self.student_list, key=lambda s: s.total_marks, reverse=True
        )
        for s in sorted_students:
            print(f"ID: {s.id}, Name: {s.name}, Marks: {s.total_marks}")
 
    # 3. Display division
    def display_division(self) -> None:
        if not self.student_list:
            print("No students available")
            return
 
        for s in self.student_list:
            if s.total_marks >= 60:
                division = "1st Division"
            elif s.total_marks >= 45:
                division = "2nd Division"
            elif s.total_marks >= 35:
                division = "3rd Division"
            else:
                division = "Fail"
 
            print(f"{s.name} ({s.total_marks}) → {division}")
 
    # 4. Count distinction students
    def count_distinction(self) -> int:
        return sum(1 for s in self.student_list if s.total_marks >= 75)
 
    # 5. Restrict students with marks < 20
    def restrict_low_scorers(self) -> None:
        before = len(self.student_list)
        self.student_list = [s for s in self.student_list if s.total_marks >= 20]
        removed = before - len(self.student_list)
        print(f"{removed} student(s) restricted (removed)")
 
 
# ---------------- MENU-DRIVEN PROGRAM ---------------- #
 
def menu():
    print("\n------ Student Management System ------")
    print("1. Add Student")
    print("2. Get Total Strength")
    print("3. Display Students (Descending Marks)")
    print("4. Display Student Divisions")
    print("5. Count Distinction Students (>=75)")
    print("6. Restrict Students (Marks < 20)")
    print("7. Exit")
 
 
def main():
    teacher = Teacher(1, "Mr. Sharma")
 
    while True:
        menu()
        choice = input("Enter your choice (1-7): ")
 
        try:
            if choice == "1":
                sid = int(input("Enter Student ID: "))
                name = input("Enter Student Name: ")
                marks = float(input("Enter Total Marks: "))
                teacher.add_student(Student(sid, name, marks))
                print("Student added successfully")
 
            elif choice == "2":
                print("Total strength:", teacher.total_strength())
 
            elif choice == "3":
                teacher.display_descending()
 
            elif choice == "4":
                teacher.display_division()
 
            elif choice == "5":
                print("Distinction count:", teacher.count_distinction())
 
            elif choice == "6":
                teacher.restrict_low_scorers()
 
            elif choice == "7":
                print("Exiting program...")
                break
 
            else:
                print("Invalid choice! Try again.")
 
        except ValueError as e:
            print("Error:", e)
 
 
if __name__ == "__main__":
    main()