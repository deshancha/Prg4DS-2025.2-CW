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

    def about(self):
        return f"{super().about()}, Department: {self.department}"

# Professor
class Professor(Faculty):
    def __init__(self, person_id, name, department, research_interest):
        super().__init__(person_id, name, department)
        if isinstance(research_interest, list):
            self.research_area = research_interest
        else:
            self.research_area = [research_interest]

# Lecturer
class Lecturer(Faculty):
    def __init__(self, person_id, name, department, teach_subjects):
        super().__init__(person_id, name, department)
        if isinstance(teach_subjects, list):
            self.teach_subjects = teach_subjects
        else:
            self.teach_subjects = [teach_subjects]
    
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
