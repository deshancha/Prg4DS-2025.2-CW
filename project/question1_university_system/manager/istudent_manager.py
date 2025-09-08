
# =======================================================
# File: istudent_manager.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

from abc import ABC, abstractmethod
from model.results import Results

# Course class, for scalability + avoid unit test modification in future
class IStudentManager(ABC):
    @abstractmethod
    def enroll(self, student, semester, course):
        pass

    @abstractmethod
    def drop(self, semester, course_code):
        pass

    @abstractmethod
    def set_results(self, results: Results):
        pass

    @abstractmethod
    def gpa(self, student) -> float:
        pass