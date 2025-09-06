# =======================================================
# File: test_faculty.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

import unittest

from domain.model.people.student import Student
from domain.model.other.course import Course
from data.manager.student_manager_imp import StudentManagerImp
from secure_student_record import SecureStudentRecord
from secure_student_record import ConstVals 
from domain.model.other.grade import Grade

# Testing Student
class TestSecureStudentRecord(unittest.TestCase):

    def setUp(self):
        self.semester = "SEM1"
        self.student = Student(
            person_id=1,
            name="Saman",
            student_id="2025CS01",
            student_manager=StudentManagerImp()
        )
        self.secure_student = SecureStudentRecord(self.student)

        self.course1 = Course("P4DSc", "Programming for Data Science")
        self.course2 = Course("DVIZ", "Data Visualization")
        self.course3 = Course("AALGO", "Advanced Algorithms")
        self.course4 = Course("NL", "Neural Networks")

    def test_enroll_ok(self):
        for course in [self.course1, self.course2, self.course3]:
            self.secure_student.enroll_course(self.semester, course)

        num_encrolled = len(self.secure_student.student.semester_courses[self.semester])
        self.assertEqual(num_encrolled, 3)

    def test_enroll_course_max_reached_and_throw_error_ok(self):
        for i in range(ConstVals.MAX_COURSES_PER_SEMESTER):
            self.secure_student.enroll_course(self.semester, Course(f"C{i}", f"Course {i}"))

        self.assertRaises(
            ValueError,
            self.secure_student.enroll_course,
            self.semester,
            self.course1
        )

    def test_gpa_calculation_ok(self):
        for course in [self.course1, self.course2, self.course3, self.course4]:
            self.secure_student.enroll_course(self.semester, course)

        self.course1.course_grade = Grade.A
        self.course2.course_grade = Grade.B
        self.course3.course_grade = Grade.B_PLUS
        self.course4.course_grade = Grade.C

        gpa = self.secure_student.gpa
        self.assertEqual(gpa, 3.07)

    def test_set_valid_gpa_ok(self):
        gpa_val = 3.75
        self.secure_student.gpa = gpa_val
        self.assertEqual(self.secure_student.gpa, gpa_val)

    def test_set_invalid_gpa_range_throw_error_ok(self):
        with self.assertRaises(ValueError):
            self.secure_student.gpa = 5.8
        with self.assertRaises(ValueError):
            self.secure_student.gpa = -1.0

    def test_set_invalid_gpa_type_throw_error_ok(self):
        with self.assertRaises(TypeError):
            self.secure_student.gpa = "String"
        with self.assertRaises(TypeError):
            self.secure_student.gpa = None

    def test_change_student_ok(self):
        new_student = Student(
            person_id=2,
            name="Kamal",
            student_id="2025CS02",
            student_manager=StudentManagerImp()
        )
        self.secure_student.student = new_student
        self.assertEqual(self.secure_student.student.name, "Kamal")

if __name__ == "__main__":
    unittest.main()