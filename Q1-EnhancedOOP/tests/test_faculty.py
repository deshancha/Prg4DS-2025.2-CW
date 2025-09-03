# =======================================================
# File: test_faculty.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

import unittest

from domain.model.people.faculty import Professor, TA, Lecturer

class TestFaculty(unittest.TestCase):
    # Prof Unit
    def test_professor_single_interest_ok(self):
        prof = Professor(1, "Prof. A", "CS", "AI")
        self.assertIsInstance(prof, Professor)
        self.assertEqual(prof.research_area, ["AI"])

    def test_professor_multiple_interests_ok(self):
        interests = ["AI", "ML"]
        prof = Professor(2, "Dr. D", "Math", interests)
        self.assertEqual(prof.research_area, interests)

    # Lecturer Unit
    def test_lecturer_single_subject_ok(self):
        lecturer = Lecturer(1, "Lec A", "CS", "Programming")
        self.assertIsInstance(lecturer, Lecturer)
        self.assertEqual(lecturer.teach_subjects, ["Programming"])

    def test_lecturer_multiple_subjects_ok(self):
        subjects = ["Programming", "Databases"]
        lecturer = Lecturer(2, "Lec B", "IT", subjects)
        self.assertEqual(lecturer.teach_subjects, subjects)

    # Ta Unit
    def test_ta_assistant_to_professor_ok(self):
        prof = Professor(1, "Prof. A", "CS", "AI")
        ta = TA(10, "TA A", "CS", prof)
        self.assertIsInstance(ta, TA)
        self.assertEqual(ta.assistant_to, prof)

    def test_ta_assistant_to_lecturer_ok(self):
        lecturer = Lecturer(2, "Lec B", "Maths", ["Algebra"])
        ta = TA(11, "TA B", "Maths", lecturer)
        self.assertEqual(ta.assistant_to, lecturer)

    def test_ta_invalid_assistant_to_raises(self):
        self.assertRaises(TypeError, TA, 12, "TA C", "IT", "Someone Else")

if __name__ == "__main__":
    unittest.main()