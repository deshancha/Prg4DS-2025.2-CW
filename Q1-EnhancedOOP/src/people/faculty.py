# =======================================================
# File: faculty.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

from .person import Person

# Faculty
class Faculty(Person):
    def __init__(self, person_id, name, department):
        super().__init__(person_id, name)
        self.department = department

    def responsibilities(self):
        return "Do Research, Teach Courses, Mentoring"

# Professor
class Professor(Faculty):
    def __init__(self, person_id, name, department, research_interest):
        super().__init__(person_id, name, department)
        if isinstance(research_interest, list):
            self.research_area = research_interest
        else:
            self.research_area = [research_interest]
    
    def get_responsibilities(self):
        return "Head of Resrach Work, Academic Leadership"

# Lecturer
class Lecturer(Faculty):
    def __init__(self, person_id, name, department, teach_subjects):
        super().__init__(person_id, name, department)
        if isinstance(teach_subjects, list):
            self.teach_subjects = teach_subjects
        else:
            self.teach_subjects = [teach_subjects]
    
    def get_responsibilities(self):
        return "Stdent Mentoring, Teaching Subjects"
    
# Teaching Assitant
class TA(Faculty):
    """
    Args:
        assistant_to (Professor or Lecturer)
    Raises:
            TypeError: If assistant_to is inalid
    """
    def __init__(self, person_id, name, department, assistant_to):
        super().__init__(person_id, name, department)
        
        if not isinstance(assistant_to, (Lecturer, Professor)):
            raise TypeError("assistant_to must be Lecturer or Professor")
        
        self.assistant_to = assistant_to
    
    def get_responsibilities(self):
        return "Assist prof or lecturers in teaching, lab works"