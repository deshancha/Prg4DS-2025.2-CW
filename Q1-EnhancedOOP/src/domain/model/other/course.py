# Course class, for scalability + avoid unit test modification in future
class Course:
    def __init__(self, code, name):
        self.course_code = code
        self.course_name = name