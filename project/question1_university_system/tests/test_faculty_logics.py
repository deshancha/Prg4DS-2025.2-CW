# =======================================================
# File: test_faculty_logics.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

import unittest

from student import Student
from model.course import Course
from faculty import Professor, TA

from manager.imp.course_manager_imp import CourseManagerImp

class TestFacultyCouseAssignement(unittest.TestCase):
    def setUp(self):
        self.manager = CourseManagerImp()
        self.course = Course(
            code="P4DSC",
            name="Programming for Data Science",
            course_manager=self.manager,
        )

    def test_assign_faculty_to_couse_success_ok(self):
        prof = Professor("PFOF_1", "Prof. Sarath", "CS", "Linear Algebra")
        ta = TA(10, "TA A", "CS", prof)

        self.course.assigned_faculty.append(prof)
        self.course.assigned_faculty.append(ta)

        self.assertIn(prof, self.course.assigned_faculty)
        self.assertIn(ta, self.course.assigned_faculty)

if __name__ == "__main__":
    unittest.main()