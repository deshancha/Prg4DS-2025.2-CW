
# =======================================================
# File: department.py
# Created by: CD
# Date: 2025-09-06
# =======================================================

class Department:
    def __init__(self, name):
        self.name = name
        self.faculty_memmbers = []
        self.courses = []
        self.students = []

    def add_faculty(self, faculty):
        if faculty in self.faculty_memmbers:
            raise ValueError(f"{faculty.name} already in ths deaprtment [{self.name}]")
        self.faculty_memmbers.append(faculty)

    def add_course(self, course):
        if course in self.courses:
            raise ValueError(f"{course.course_code} already in ths deaprtment [{self.name}] course list")
        self.courses.append(course)

    def add_student(self, student):
        if student in self.students:
            raise ValueError(f"{student.name} already in ths deaprtment [{self.name}] student list")
        self.students.append(student)