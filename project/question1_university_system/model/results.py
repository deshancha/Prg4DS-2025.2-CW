
from .grade import Grade

class Results:
    def __init__(self, semester, course_code, grade):
        self.semester = semester
        self.course_code = course_code
        self.course_grade = grade