
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

    def add_faculty(self, faculty):
        self.faculty_memmbers.append(faculty)

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)