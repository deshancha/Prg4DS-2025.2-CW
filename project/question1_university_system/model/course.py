# =======================================================
# File: course.py
# Created by: CD
# Date: 2025-09-06
# =======================================================


from .grade import Grade
from typing import List, Optional
from manager.icourse_manager import ICourseManager

# Course class, for scalability + avoid unit test modification in future
class Course:
    def __init__(self, code,
                name,
                credits = 3,
                max_students_allowd = 10,
                should_have_completed: List[str] = None,
                course_manager: ICourseManager | None = None):
        self.course_code = code
        self.course_name = name
        self.course_credits = credits
        self.max_students_allowd = max_students_allowd
        self.reading_students: List[str] = []
        self.should_have_completed = should_have_completed
        self._course_manager: ICourseManager | None = course_manager

    def add_student(self, person_id: str, completed_courses: List[str]):
        self._course_manager.add_student(self, person_id, completed_courses)