
# =======================================================
# File: istudent_manager.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

from abc import ABC, abstractmethod

class IStudentManager(ABC):
    @abstractmethod
    def enroll(self, student, semester, course):
        pass

    @abstractmethod
    def drop(self, semester, course_code):
        pass