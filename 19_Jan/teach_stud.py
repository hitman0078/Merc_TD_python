"""student and teachers """
class Student:
    def __init__(self, id: int, name: str, total_marks: float):
        self.__id = id
        self.__name = name
        self.__total_marks = total_marks
 
class Teacher:
    def __init__(self, id: int, name: str, student_list: Optional[List[Student]] = None):
        self.id = id
        self.name = name
        self.student_list = student_list if student_list is not None else []
 
    # ---- Useful functions (methods) ----
    def add_student(self, student: Student) -> None:
        """Add a student if not already present by id."""
        if any(s.id == student.id for s in self.student_list):
            raise ValueError(f"Student with id={student.id} already exists.")
        self.student_list.append(student)
 
    def remove_student(self, student_id: int) -> None:
        """Remove a student by id."""
        before = len(self.student_list)
        self.student_list = [s for s in self.student_list if s.id != student_id]
        if len(self.student_list) == before:
            raise ValueError(f"No student found with id={student_id}.")
 
    def get_student(self, student_id: int) -> Optional[Student]:
        """Fetch a student by id."""
        return next((s for s in self.student_list if s.id == student_id), None)
 