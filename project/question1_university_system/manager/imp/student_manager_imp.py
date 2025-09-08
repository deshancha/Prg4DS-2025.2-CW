from ..istudent_manager import IStudentManager
from model.results import Results
from logger.logger import Logger

class StudentManagerImp(IStudentManager):

    # Enroll Course
    def enroll(self, student, semester, course):
        if semester not in student.semester_courses:
            student.semester_courses[semester] = {}

        if course.course_code in student.semester_courses[semester]:
            raise ValueError( f"{student.name}, already enrolled in Course:[{course.course_code}-{course.course_name}] Sem: {semester}" )
        
        # completed coursed of the student to validate prerequisites
        completed_courses = [result.course_code for result in student.course_results]

        # TODO: add student to course here
        course.add_student(student.person_id, completed_courses)

        student.semester_courses[semester][course.course_code] = course
        Logger.info(f"{student.name} enrolled in {course.course_code} for {semester}")

    # Remove Course
    def drop(self, student, semester, course_code):
        if semester not in student.semester_courses or course_code not in student.semester_courses[semester]:
            raise ValueError(f"{course_code}\t not found in {semester} courses for {student.name}")
        
        del student.semester_courses[semester][course_code]
        Logger.info(f"{student.name} removed {course_code}\tfrom {semester}")


    # Setting Results and validations
    def set_results(self, student, result: Results):
        # courses in semester
        courses_in_semester = self._get_courses(student, result.semester)

        # if setting result related course not exist in semester we thor error
        if result.course_code not in courses_in_semester:
            raise ValueError(
                f"{result.course_code} not found in {result.semester} courses for {student.name}"
            )
        
        # if results already set for course in the semester we throw error
        for exisitng_resutls in student._course_results:
            if exisitng_resutls.semester == result.semester and exisitng_resutls.course_code == result.course_code:
                raise ValueError(
                    f"Result for {result.course_code} in {result.semester} already exists for {student.name}"
                )

        student._course_results.append(result)
        Logger.info(f"Set results for {student.name} [{result.course_grade}\t{result.course_code} from {result.semester}]")

    # Calculate GPA
    def gpa(self, student) -> float:
        total_points = 0.0
        total_credits = 0.0
        
        for result in student._course_results:
            courses_in_semester = self._get_courses(student, result.semester)
            course = courses_in_semester.get(result.course_code)

            # course in not null, we check the existance of course in set_results

            total_points += result.course_grade.value * course.course_credits
            total_credits += course.course_credits
        
        if total_credits == 0:
            raise ValueError(f"No graded courses found for {student.name}. GPA cannot be calculated")
    
        gpa = round(total_points / total_credits, 2)

        Logger.info(f"{student.name}'s\t GPA: {gpa}")

        return gpa
    

    # Helper for return sememster courses
    def _get_courses(self, student, semester):
        return student.semester_courses.get(semester, {})