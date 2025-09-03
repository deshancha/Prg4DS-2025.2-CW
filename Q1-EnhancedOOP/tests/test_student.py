# =======================================================
# File: test_faculty.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

import unittest

from people.student import Student
from model import AcademicStatus

class TestStudent(unittest.TestCase):

    def test_initial_academic_status_is_na_ok(self):
        student = Student(1, "Studnet A", "2025CS01")
        self.assertEqual(student.get_academic_status(), AcademicStatus.NA)

if __name__ == "__main__":
    unittest.main()