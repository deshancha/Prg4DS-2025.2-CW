from domain.manager.istudent_manager import IStudentManager

# This is a friend class for Student
class StudentManagerImp(IStudentManager):

    def enroll(self, student, semester, course):
        if semester not in student._semester_courses:
            student._semester_courses[semester] = {}

        if course.course_code in student._semester_courses[semester]:
            raise ValueError( f"{student.name}, already enrolled in Course:[{course.course_code}-{course.course_name}] Sem: {semester}" )

        student._semester_courses[semester][course.course_code] = course
        print(f"{student.name} enrolled in {course.course_code} for {semester}.")

    def drop(self, student, semester, course_code):
        if semester not in student._semester_courses or course_code not in student._semester_courses[semester]:
            raise ValueError(f"{course_code} not found in {semester} courses for {student.name}.")
        
        del student._semester_courses[semester][course_code]
        print(f"{student.name} removed {course_code} from {semester}.")