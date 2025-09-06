# =======================================================
# File: test_faculty.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

import unittest

from student import Student
from model.course import Course
from model.academic_status import AcademicStatus
from model.grade import Grade
from manager.student_manager_imp import StudentManagerImp

# Testing Student Enrollement
class TestStudentEnrollment(unittest.TestCase):
    def setUp(self):
        self.semester = "SEM_1"
        self.manager = StudentManagerImp()
        self.student = Student(1, "Studnet A", "2025CS01", self.manager)
        self.course = Course("P4DSC", "Programming for Data Sciecne")

    def test_enroll_new_course_ok(self):
        self.student.enroll_course(self.semester, self.course)
        self.assertIn(self.semester, self.student._semester_courses)
        self.assertIn("P4DSC", self.student._semester_courses[self.semester])

    def test_enroll_existing_course_raise_error_ok(self):
        # enroll
        self.student.enroll_course(self.semester, self.course)
        # and try enroll again should raise error
        self.assertRaises(
            ValueError,
            self.student.enroll_course,
            self.semester,
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


# Testing Student Gpa Calc
class TestCalculateGPA(unittest.TestCase):
    def setUp(self):
        self.semester = "SEM_1"
        self.student = Student(1, "Saman", "2025CS01", StudentManagerImp())
        self.course1_grade = 4
        self.course2_grade = 5
        self.course1 = Course("P4DSC", "Programming for Data Sciecne", self.course1_grade)
        self.course2 = Course("DATA_VIS", "Data Visualization", self.course2_grade)

    def test_calculate_gpa_with_grades_ok(self):
        # Set Grades
        self.course1.course_grade = Grade.A
        self.course2.course_grade = Grade.C_PLUS

        # Enroll
        self.student.enroll_course(self.semester, self.course1)
        self.student.enroll_course(self.semester, self.course2)

        # GPA
        gpa = self.student.calculate_gpa()

        # expcted gpa calc
        total_points = self.course1_grade * Grade.A.value + self.course2_grade * Grade.C_PLUS.value
        total_credits = self.course1_grade + self.course2_grade
        expected_gpa = round(total_points / total_credits, 2)

        self.assertEqual(gpa, expected_gpa)
        self.assertEqual(self.student.gpa, expected_gpa)

    def test_calculate_gpa_no_grades_raise_error_ok(self):
        # Not setting Grades

        # Enroll
        self.student.enroll_course(self.semester, self.course1)
        self.student.enroll_course(self.semester, self.course2)

        # without setting grade for a course, calculating gpa is meaningless
        self.assertRaises(
            ValueError,
            self.student.calculate_gpa,
        )

# Testing Student Academic Status
class TestStudentAcademicStatus(unittest.TestCase):
    def setUp(self):
        self.semester = "SEM_1"
        self.student = Student(1, "Nimal", "2025CS01", StudentManagerImp())
        self.course = Course("P4DSC", "Programming for Data Sciecne", 3)

    def test_academic_status_deans_list_ok(self):
        # Enrol Coause
        self.student.enroll_course(self.semester, self.course)

        # set GPA 4.0 Grade.A
        self.course.course_grade = Grade.A        

        self.student.calculate_gpa()
        self.assertEqual(self.student.get_academic_status(), AcademicStatus.DEANS_LIST)

    def test_academic_status_good_ok(self):
        # Enrol Coause
        self.student.enroll_course(self.semester, self.course)

        # set GPA 3.0 Grade.B
        self.course.course_grade = Grade.B        

        self.student.calculate_gpa()
        self.assertEqual(self.student.get_academic_status(), AcademicStatus.GOOD)

    def test_academic_status_probation_ok(self):
        # Enrol Coause
        self.student.enroll_course(self.semester, self.course)

        # set GPA 1.0 Grade.D
        self.course.course_grade = Grade.D        

        self.student.calculate_gpa()
        
        self.assertEqual(self.student.get_academic_status(), AcademicStatus.PROBATION)


if __name__ == "__main__":
    unittest.main()