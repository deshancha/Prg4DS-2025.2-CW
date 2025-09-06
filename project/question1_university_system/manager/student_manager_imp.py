from .istudent_manager import IStudentManager

# This is a friend class for Student
class StudentManagerImp(IStudentManager):

    # Enroll Course
    def enroll(self, student, semester, course):
        if semester not in student.semester_courses:
            student.semester_courses[semester] = {}

        if course.course_code in student.semester_courses[semester]:
            raise ValueError( f"{student.name}, already enrolled in Course:[{course.course_code}-{course.course_name}] Sem: {semester}" )

        student.semester_courses[semester][course.course_code] = course
        print(f"{student.name} enrolled in {course.course_code} for {semester}.")

    # Remove Course
    def drop(self, student, semester, course_code):
        if semester not in student.semester_courses or course_code not in student.semester_courses[semester]:
            raise ValueError(f"{course_code} not found in {semester} courses for {student.name}.")
        
        del student.semester_courses[semester][course_code]
        print(f"{student.name} removed {course_code} from {semester}.")

    # Calculate GPA
    def gpa(self, student) -> float:
        total_points = 0.0
        total_credits = 0.0
        
        for semester_courses in student.semester_courses.values():
            for course in semester_courses.values():
                if course.course_grade is None:
                    continue
                total_points += course.course_grade.value * course.course_credits
                total_credits += course.course_credits
        
        if total_credits == 0:
            raise ValueError(f"No graded courses found for {student.name}. GPA cannot be calculated.")
    
        gpa = round(total_points / total_credits, 2) if total_credits > 0 else 0.0

        print(f"{student.name}'s GPA: {gpa}")

        return gpa