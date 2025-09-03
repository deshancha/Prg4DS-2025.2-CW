from .person import Person
from domain.model.other.academic_status import AcademicStatus
from domain.manager.istudent_manager import IStudentManager

class Student(Person):
    def __init__(self, person_id, name, student_id, student_manager):
        super().__init__(person_id, name)
        self.student_id = student_id
        self._semester_courses = {} # { "SEM_1": { "P4DSC": Course() } }
        self._gpa = 0.0
        self._academic_status = AcademicStatus.NA
        self._student_manager = student_manager

    def about(self):
        return f"{super().about()}, Std ID: {self.student_id}"
    
    def get_academic_status(self):
        return self._academic_status
    
    def enroll_course(self, semester, course):
        self._student_manager.enroll(self, semester, course)

class UndergraduateStudent(Student):
    def __init__(self, person_id, name, student_id):
        super().__init__(person_id, name, student_id)

class GraduateStudent(Student):
    def __init__(self, person_id, name, student_id):
        super().__init__(person_id, name, student_id)