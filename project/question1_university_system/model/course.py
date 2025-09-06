# =======================================================
# File: course.py
# Created by: CD
# Date: 2025-09-06
# =======================================================


from .grade import Grade

# Course class, for scalability + avoid unit test modification in future
class Course:
    def __init__(self, code, name, credits = 3):
        self.course_code = code
        self.course_name = name
        self.course_credits = credits