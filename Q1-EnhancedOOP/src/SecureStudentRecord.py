from domain.model.people.student import Student
from domain.model.other.course import Course
from domain.model.other.grade import Grade
from data.manager.student_manager_imp import StudentManagerImp

class _ConstVals:    
    MAX_COURSES_PER_SEMESTER = 4

class SecureStudentRecord:
    def __init__(self, student: Student):
        self._reset(student)

    def _reset(self, student: Student):
        self._student = student
        self._gpa: float | None = None

    # Setter/getter for student
    @property
    def student(self) -> Student:
        return self._student

    @student.setter
    def student(self, new_student: Student):
        if not isinstance(new_student, Student):
            raise TypeError("Assigned value must be a Student instance.")
        self._reset(new_student)

    # gpa getter
    @property
    def gpa(self) -> float:
        if self._gpa is None:
            self._gpa = self._student.calculate_gpa()
        return self._gpa
    
    # allow set gpa from outside 
    @gpa.setter
    def gpa(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("GPA must be a number.")
        if not (0.0 <= value <= 4.0):
            raise ValueError("GPA must be between 0.0 and 4.0.")
        
        # now gpa getter always return this value
        self._gpa = round(float(value), 2)
    
    # validation
    def enroll_course(self, semester, course: Course):
        if semester not in self._student._semester_courses:
            self._student._semester_courses[semester] = {}

        if len(self._student._semester_courses[semester]) >= _ConstVals.MAX_COURSES_PER_SEMESTER:
            raise ValueError(f"Cannot enroll in more than {_ConstVals.MAX_COURSES_PER_SEMESTER} courses in {semester}.")

        self._student.enroll_course(semester, course)



if __name__ == "__main__":
    student = Student(person_id=1, name="Saman", student_id="2025CS01", student_manager=StudentManagerImp())

    secure_student = SecureStudentRecord(student)

    course1 = Course("P4DSc", "Programming for Data Sceince")
    course2 = Course("DVIZ", "Data Visialization")
    course3 = Course("AALGO", "Advanced Algorithms")
    course4 = Course("NL", "Neural Networks")

    semster = "SEM1"

    semesterCourses = [course1, course2, course3, course4]

    # ok to enter 4
    for course in [course1, course2, course3]:
        try:
            secure_student.enroll_course(semster, course)
        except ValueError as e:
            print(f"Enrollment error: {e}")

    # should fail
    for course in [course1, course2, course3]:
        try:
            secure_student.enroll_course(semster, course)
        except ValueError as e:
            print(f"Enrollment error: {e}")
            break

    # assign grades and get gpa
    course1.course_grade = Grade.A  
    course2.course_grade = Grade.B
    course3.course_grade = Grade.B_PLUS
    course4.course_grade = Grade.C

    try:
        print(f"{secure_student.student.name}'s GPA: {secure_student.gpa}")
    except ValueError as e:
        print(f"GPA error: {e}")

    # assign invalid gpa invalid range
    try:
        secure_student.gpa = 5.8
    except (TypeError, ValueError) as e:
        print(f"GPA set error: {e}")

    # assign invalid gpa invalid type
    try:
        secure_student.gpa = "3"
    except (TypeError, ValueError) as e:
        print(f"GPA set error: {e}")



