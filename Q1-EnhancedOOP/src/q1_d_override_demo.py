from domain.model.people.student import *
from domain.model.people.faculty import *


class _DummyManager(IStudentManager):
    def enroll(self, student, semester, course): pass
    def drop(self, student, semester, course): pass
    def gpa(self, student): return 4.0


if __name__ == "__main__":
    student = Student(1, "Saman", "2025CS01", _DummyManager())
    professor = Professor(2, "Prof. Prasad", "Computer Science", ["AI", "ML"])
    lecturer = Lecturer(3, "Dr. Ruwan", "Maths", ["Calculus", "Linear Algebra"])
    ta = TA(4, "Kasun", "Computer Science", professor)

    people = [student, professor, lecturer, ta]

    for person in people:
        print(person.get_responsibilities())

    faculty_members = [professor, lecturer, ta]

    for fac_mem in faculty_members:
        print(f"{fac_mem.name} Workload: {fac_mem.calculate_workload()} hrs")