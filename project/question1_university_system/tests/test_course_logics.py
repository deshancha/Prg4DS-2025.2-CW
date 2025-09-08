# =======================================================
# File: test_course_logics.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

import unittest

from model.course import Course
from manager.imp.course_manager_imp import CourseManagerImp

class TestCourseAddRemoveStudent(unittest.TestCase):
    def setUp(self):
        self.manager = CourseManagerImp()
        self.course_credits = 7
        self.max_allowed_students = 25
        self.should_have_completed = ["BASIC_001", "BASIC_003"]
        self.course = Course(
            code="P4DSC",
            name="Programming for Data Science",
            credits=self.course_credits,
            max_students_allowd=self.max_allowed_students,
            should_have_completed=self.should_have_completed,
            course_manager=self.manager,
        )
        self.student_id = "STUDENT_01"

    def test_add_student_success_ok(self):
        completed = ["BASIC_001", "BASIC_003", "BASIC_002"]
        self.course.add_student(self.student_id, completed)
        self.assertIn(self.student_id, self.course.reading_students)

    def test_add_student_prerequisites_not_completed_raises_error_ok(self):
        completed = ["BASIC_002"]
        self.assertRaises(
            ValueError,
            self.course.add_student,
            self.student_id,
            completed
        )

    def test_add_student_exceds_max_alowed_raises_error_ok(self):
        for i in range(self.max_allowed_students):
            self.course.add_student(f"ST{i}", self.should_have_completed)
        
        self.assertRaises(
            ValueError,
            self.course.add_student,
            "TEMP_ID",
            self.should_have_completed
        )
    
    def test_remove_student_ok(self):
        self.course.add_student(self.student_id, self.should_have_completed)
        self.course.remove_student(self.student_id)
        self.assertNotIn(self.student_id, self.course.reading_students)

    def test_remove_student_not_found_raises_error_ok(self):
        self.assertRaises(
            ValueError,
            self.course.remove_student,
            "TEMP_ID"
        )


if __name__ == "__main__":
    unittest.main()