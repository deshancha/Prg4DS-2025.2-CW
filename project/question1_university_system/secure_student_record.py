# =======================================================
# File: secure__student_record.py
# Created by: CD
# Date: 2025-09-06
# =======================================================


from student import Student
from model.course import Course

class ConstVals:    
    MAX_COURSES_PER_SEMESTER = 4

class SecureStudentRecord:
    def __init__(self, student: Student):
        self._reset(student)

    def _reset(self, student: Student):
        self.__student = student
        self.__gpa: float | None = None

    # Setter/getter for student
    @property
    def student(self) -> Student:
        return self.__student

    @student.setter
    def student(self, new__student: Student):
        if not isinstance(new__student, Student):
            raise TypeError("Assigned value must be a Student instance.")
        self._reset(new__student)

    # gpa getter
    @property
    def gpa(self) -> float:
        if self.__gpa is None:
            self.__gpa = self.__student.calculate_gpa()
        return self.__gpa
    
    # allow set gpa from outside 
    @gpa.setter
    def gpa(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("GPA must be a number.")
        if not (0.0 <= value <= 4.0):
            raise ValueError("GPA must be between 0.0 and 4.0.")
        
        # now gpa getter always return this value
        self.__gpa = round(float(value), 2)
    
    # validation
    def enroll_course(self, semester, course: Course):
        if semester not in self.__student._semester_courses:
            self.__student._semester_courses[semester] = {}

        if len(self.__student._semester_courses[semester]) >= ConstVals.MAX_COURSES_PER_SEMESTER:
            raise ValueError(f"Cannot enroll in more than {ConstVals.MAX_COURSES_PER_SEMESTER} courses in {semester}.")

        self.__student.enroll_course(semester, course)
