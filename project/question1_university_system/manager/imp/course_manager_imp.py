from ..icourse_manager import ICourseManager
from logger.logger import Logger
from typing import List
from faculty import Faculty

class CourseManagerImp(ICourseManager):

    # Assign Student to Course
    def add_student(self, course, person_id: str, completed_courses: List[str]):
        course_code = course.course_code

        # check meets the prerequsites
        if course.should_have_completed is not None:
            for required in course.should_have_completed:
                if required not in completed_courses:
                    raise ValueError(f"Cannot enroll:{person_id} prerequisite {required} not completed for {course_code}")
        
        # check maximum allowed reached
        if len(course.reading_students) >= course.max_students_allowd:
            raise ValueError(f"Course {course_code} reached maximum allowed limit[{course.max_students_allowd}]")
        
        course.reading_students.append(person_id)

    # Remove Student frm course
    def remove_student(self, course, person_id: str):
        if person_id not in course.reading_students:
            raise ValueError(f"Student {person_id} not assigned to corse:[{course.course_code}]")

        course.reading_students.remove(person_id)

    # assign Faculty to Course
    def assign_faculty(self, course, faculty: Faculty):
        if faculty in course.assigned_faculty:
            raise ValueError(f"Faculty {faculty.name} already assigned to {course.course_code}")
        
        course.assigned_faculty.append(faculty)