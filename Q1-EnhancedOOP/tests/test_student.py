# =======================================================
# File: test_faculty.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

import unittest

from domain.model.people.student import Student
from domain.model.other.course import Course
from domain.model.other.academic_status import AcademicStatus
from data.manager.student_manager_imp import StudentManagerImp

# Testing Student
class TestStudent(unittest.TestCase):

    def test_initial_academic_status_is_not_applied_ok(self):
        student = Student(1, "Studnet A", "2025CS01", None)
        self.assertEqual(student.get_academic_status(), None)

if __name__ == "__main__":
    unittest.main()