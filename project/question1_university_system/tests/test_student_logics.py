# =======================================================
# File: test_faculty.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

import unittest

from student import UndergraduateStudent
from model.course import Course
from model.academic_status import AcademicStatus
from model.grade import Grade
from model.results import Results
from manager.imp.student_manager_imp import StudentManagerImp
from manager.imp.course_manager_imp import CourseManagerImp

# Testing Student Enrollement
class TestStudentEnrollment(unittest.TestCase):
    def setUp(self):
        self.semester = "SEM_1"
        self.student = UndergraduateStudent(1, "Studnet A", "2025CS01", StudentManagerImp())
        self.course = Course("P4DSC", "Programming for Data Sciecne", course_manager = CourseManagerImp())

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
        self.student = UndergraduateStudent(1, "student A", "2025CS01", StudentManagerImp())
        self.course = Course(self.course_code, "Programming for Data Sciecne", course_manager = CourseManagerImp())
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
        self.student = UndergraduateStudent(1, "Saman", "2025CS01", StudentManagerImp())
        self.course1_grade = 4
        self.course2_grade = 5
        self.course1 = Course("P4DSC", "Programming for Data Sciecne", self.course1_grade, course_manager = CourseManagerImp())
        self.course2 = Course("DATA_VIS", "Data Visualization", self.course2_grade, course_manager = CourseManagerImp())

    def test_calculate_gpa_with_grades_ok(self):
        # Enroll
        self.student.enroll_course(self.semester, self.course1)
        self.student.enroll_course(self.semester, self.course2)

        # Set Results
        self.student.set_results(Results(self.semester, self.course1.course_code, Grade.A ))
        self.student.set_results(Results(self.semester, self.course2.course_code, Grade.C_PLUS ))

        # GPA
        gpa = self.student.calculate_gpa()

        # expcted gpa calc
        total_points = self.course1_grade * Grade.A.value + self.course2_grade * Grade.C_PLUS.value
        total_credits = self.course1_grade + self.course2_grade
        expected_gpa = round(total_points / total_credits, 2)

        self.assertEqual(gpa, expected_gpa)
        self.assertEqual(self.student.gpa, expected_gpa)

    def test_calculate_gpa_no_grades_raise_error_ok(self):
        # Enroll
        self.student.enroll_course(self.semester, self.course1)
        self.student.enroll_course(self.semester, self.course2)

        # Not setting Grades

        # without setting grade for a course, calculating gpa is meaningless
        self.assertRaises(
            ValueError,
            self.student.calculate_gpa,
        )

# Testing Student Academic Status
class TestStudentAcademicStatus(unittest.TestCase):
    def setUp(self):
        self.semester = "SEM_1"
        self.course_code = "P4DSC"
        self.student = UndergraduateStudent(1, "Nimal", "2025CS01", StudentManagerImp())
        self.course = Course(self.course_code, "Programming for Data Sciecne", course_manager = CourseManagerImp())

    def test_academic_status_deans_list_ok(self):
        # Enrol Coause
        self.student.enroll_course(self.semester, self.course)

        # set GPA 4.0 Grade.A
        self.student.set_results(Results(self.semester, self.course_code, Grade.A ))

        self.student.calculate_gpa()
        self.assertEqual(self.student.get_academic_status(), AcademicStatus.DEANS_LIST)

    def test_academic_status_good_ok(self):
        # Enrol Coause
        self.student.enroll_course(self.semester, self.course)

        # set GPA 3.0 Grade.B
        self.student.set_results(Results(self.semester, self.course_code, Grade.B ))

        self.student.calculate_gpa()
        self.assertEqual(self.student.get_academic_status(), AcademicStatus.GOOD)

    def test_academic_status_probation_ok(self):
        # Enrol Coause
        self.student.enroll_course(self.semester, self.course)

        # set GPA 1.0 Grade.D
        self.student.set_results(Results(self.semester, self.course_code, Grade.D ))

        self.student.calculate_gpa()
        
        self.assertEqual(self.student.get_academic_status(), AcademicStatus.PROBATION)

# Testing Student setting results
class TestStudentSetResults(unittest.TestCase):
    def setUp(self):
        self.semester = "SEM_1"
        self.student = UndergraduateStudent(1, "Saman", "2025CS01", StudentManagerImp())
        self.course1 = Course("P4DSC", "Programming for Data Science", course_manager = CourseManagerImp())
        self.course2 = Course("DATA_VIS",  "Data Visualization", course_manager = CourseManagerImp())

        # Enroll courses
        self.student.enroll_course(self.semester, self.course1)
        self.student.enroll_course(self.semester, self.course2)

    def test_set_results_success_ok(self):
        result1 = Results(self.semester, self.course1.course_code, Grade.A)
        result2 = Results(self.semester, self.course2.course_code, Grade.B_PLUS)

        self.student.set_results(result1)
        self.student.set_results(result2)

        added_result1 = next(resl for resl in self.student.course_results if resl.course_code == self.course1.course_code)
        added_result2 = next(resl for resl in self.student.course_results if resl.course_code == self.course2.course_code)

        self.assertEqual(added_result1.course_grade, Grade.A)
        self.assertEqual(added_result2.course_grade, Grade.B_PLUS)

    def test_set_results_course_not_enrolled_raises_error(self):
        fake_result = Results(self.semester, "Some Not Existing Course", Grade.A)

        self.assertRaises(
            ValueError,
            self.student.set_results,
            fake_result
        )

    def test_set_duplicate_resut_raises_error(self):
        result = Results(self.semester, self.course1.course_code, Grade.A)
        self.student.set_results(result)

        self.assertRaises(
            ValueError,
            self.student.set_results,
            result
        )

if __name__ == "__main__":
    unittest.main()