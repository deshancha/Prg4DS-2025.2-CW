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

    # override
    def get_responsibilities(self):
        return "Responsibilities of Factulty goes here"
    
    def calculate_workload(self):
        return 10

# Professor
class Professor(Faculty):
    def __init__(self, person_id, name, department, research_interest):
        super().__init__(person_id, name, department)
        if isinstance(research_interest, list):
            self.research_area = research_interest
        else:
            self.research_area = [research_interest]

    # override
    def get_responsibilities(self):
        return f"Responsibilities of Professor[{self.name}] goes here"
    
    def calculate_workload(self):
        return super().calculate_workload() + 50

# Lecturer
class Lecturer(Faculty):
    def __init__(self, person_id, name, department, teach_subjects):
        super().__init__(person_id, name, department)
        if isinstance(teach_subjects, list):
            self.teach_subjects = teach_subjects
        else:
            self.teach_subjects = [teach_subjects]

    # override
    def get_responsibilities(self):
        return f"Responsibilities of Lecturer[{self.name}] goes here"
    
    # override
    def calculate_workload(self):
        return super().calculate_workload() + 40
    
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

    # override
    def get_responsibilities(self):
        return f"Responsibilities of TA[{self.name}] goes here"
    
    # override
    def calculate_workload(self):
        return super().calculate_workload() + 30