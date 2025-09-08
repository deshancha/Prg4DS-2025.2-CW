
# =======================================================
# File: istudent_manager.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

from abc import ABC, abstractmethod
from typing import List
from faculty import Faculty

# Course Logic interface, to seperate student logics from Student model class
class ICourseManager(ABC):
    @abstractmethod
    def add_student(self, course, person_id: str, completed_courses: List[str]):
        pass

    @abstractmethod
    def remove_student(self, course, person_id: str):
        pass

    @abstractmethod
    def assign_faculty(self, course, faculty: Faculty):
        pass