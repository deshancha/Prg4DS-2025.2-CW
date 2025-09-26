
# =======================================================
# File: istudent_manager.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

from abc import ABC, abstractmethod
from model.results import Results

# Student Logic interface, to seperate student logics from Student model class
class IStudentManager(ABC):
    """Interface for student management operations."""


    @abstractmethod
    def enroll(self, student, semester, course):
        """
        Enroll a student in a specific course for a given semester.
        
        Args:
            student: The student object to enroll.
            semester: The semester in which the student is enrolling.
            course: The course object in which the student is enrolling.
        """
        pass

    @abstractmethod
    def drop(self, semester, course_code):
        """
        Drop a course for a student in a specific semester.
        
        Args:
            semester: The semester from which to drop the course.
            course_code: The code of the course to be dropped.
        """
        pass

    @abstractmethod
    def set_results(self, results: Results):
        """
        Assign or update results for a student.
        
        Args:
            results: A Results object containing course grades and semester info.
        """
        pass

    @abstractmethod
    def gpa(self, student) -> float:
        """
        Calculate and return the GPA for a student.
        
        Args:
            student: The student object whose GPA is being calculated.
        
        Returns:
            A float representing the student's GPA.
        """
        pass