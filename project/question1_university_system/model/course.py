# =======================================================
# File: course.py
# Created by: CD
# Date: 2025-09-06
# =======================================================


from .grade import Grade
from typing import List, Optional

# Course class, for scalability + avoid unit test modification in future
class Course:
    def __init__(self, code, name, credits = 3, max_students_allowd = 10, should_have_completed: List[str] = None):
        self.course_code = code
        self.course_name = name
        self.course_credits = credits

        self.max_students_allowd = max_students_allowd
        self.reading_students: List[str] = []
        self.should_have_completed = should_have_completed

    def add_student(self, person_id: str, completed_courses: List[str]):

        # check meets the prerequsites
        if self.should_have_completed is not None:
            for required in self.should_have_completed:
                if required not in completed_courses:
                    raise ValueError(f"Cannot enroll:{person_id} prerequisite {required} not completed for {self.course_code}")
        
        # check maximum allowed reached
        if len(self.reading_students) >= self.max_students_allowd:
            raise ValueError(f"Course {self.course_code} reached maximum allowed limit[{self.max_students_allowd}]")