# =======================================================
# File: academic_status.py
# Created by: CD
# Date: 2025-09-06
# =======================================================


from enum import Enum

class AcademicStatus(Enum):
    GOOD = "Good Standing"
    PROBATION = "Probation"
    DEANS_LIST = "Deans List"

    @staticmethod
    def from_gpa(gpa: float):
        if gpa >= 3.5:
            return AcademicStatus.DEANS_LIST
        elif gpa < 2.0:
            return AcademicStatus.PROBATION
        else:
            return AcademicStatus.GOOD