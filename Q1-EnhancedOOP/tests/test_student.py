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
        self.assertEqual(student.get_academic_status(), AcademicStatus.NA)

# Testing Student Enrollement
class TestStudentEnrollment(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManagerImp()
        self.student = Student(1, "Studnet A", "2025CS01", self.manager)
        self.course = Course("P4DSC", "Programming for Data Sciecne")

    def test_enroll_new_course_ok(self):
        semester = "SEM_1"
        self.student.enroll_course(semester, self.course)
        self.assertIn(semester, self.student._semester_courses)
        self.assertIn("P4DSC", self.student._semester_courses[semester])

    def test_enroll_existing_course_raise_error_ok(self):
        semester = "SEM_1"
        # enroll
        self.student.enroll_course(semester, self.course)
        # and try enroll again should raise error
        self.assertRaises(
            ValueError,
            self.student.enroll_course,
            semester,
            self.course
        )

# Testing Student Drop Course
class TestStudentDropCourse(unittest.TestCase):
    def setUp(self):
        self.semester = "SEM_1"
        self.course_code = "P4DSC"
        self.student = Student(1, "student A", "2025CS01", StudentManagerImp())
        self.course = Course(self.course_code, "Programming for Data Sciecne")
        self.student.enroll_course(self.semester, self.course)

    def test_drop_existing_course_ok(self):
        self.student.drop_course(self.semester, self.course.course_code)
        self.assertNotIn(self.course_code, self.student._semester_courses[self.semester])

    def test_drop_nonexist_course_raises_error_ok(self):
        self.assertRaises(
            ValueError,
            self.student.drop_course,
            self.semester,
            "Not existinbg course code"
        )
if __name__ == "__main__":
    unittest.main()