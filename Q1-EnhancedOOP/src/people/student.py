from .person import Person
from model import AcademicStatus

class Student(Person):
    def __init__(self, person_id, name, student_id):
        super().__init__(person_id, name)
        self.student_id = student_id
        self._courses = {}
        self._gpa = 0.0
        self._academic_status = AcademicStatus.NA

    def about(self):
        return f"{super().about()}, Std ID: {self.student_id}"
    
    def get_academic_status(self):
        return self._academic_status

class UndergraduateStudent(Student):
    def __init__(self, person_id, name, student_id):
        super().__init__(person_id, name, student_id)

class GraduateStudent(Student):
    def __init__(self, person_id, name, student_id):
        super().__init__(person_id, name, student_id)