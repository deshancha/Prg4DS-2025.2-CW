from person import Person
from model.academic_status import AcademicStatus
from manager.istudent_manager import IStudentManager

class Student(Person):
    def __init__(self, person_id, name, student_id, student_manager):
        super().__init__(person_id, name)
        self.student_id = student_id
        self._semester_courses = {}
        self._gpa = 0.0
        self._academic_status: AcademicStatus | None = None
        self._student_manager: IStudentManager | None = student_manager

    @property
    def semester_courses(self):
        return self._semester_courses

    def get_academic_status(self) -> AcademicStatus:
        return self._academic_status
    
    def enroll_course(self, semester, course):
        self._student_manager.enroll(self, semester, course)

    def drop_course(self, semester, course_code):
        self._student_manager.drop(self, semester, course_code)

    def calculate_gpa(self) -> float:
        self.gpa = self._student_manager.gpa(self)
        self._academic_status = AcademicStatus.from_gpa(self.gpa)
        return self.gpa
    
    # override
    def get_responsibilities(self):
        return f"Responsibilities of Student[{self.name}] goes here"
    

class UndergraduateStudent(Student):
    def __init__(self, person_id, name, student_id):
        super().__init__(person_id, name, student_id)

    # override
    def get_responsibilities(self):
        return f"Responsibilities of UndergraduateStudent[{self.name}] goes here"

class GraduateStudent(Student):
    def __init__(self, person_id, name, student_id):
        super().__init__(person_id, name, student_id)

    # override
    def get_responsibilities(self):
        return f"Responsibilities of GraduateStudent[{self.name}] goes here"