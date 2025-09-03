# =======================================================
# File: main.py
# Created by:CD
# Date: 2025-09-03
# =======================================================

from domain.model.people.faculty import Professor
from domain.model.people.student import Student

def main():
    interests = ["AI", "ML"]
    prof = Professor(2, "Dr. D", "Math", interests)
    print(prof.about())
    student = Student(2, "Saman", "2025CS01")
    print(student.about())

if __name__ == "__main__":
    main()
