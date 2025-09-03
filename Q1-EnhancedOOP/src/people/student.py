from .person import Person

class Student(Person):
    def __init__(self, person_id, name, student_id):
      super().__init__(person_id, name)
      self.student_id = student_id

    def about(self):
        return f"{super().about()}, Std ID: {self.student_id}"

class UndergraduateStudent(Student):
    def __init__(self, person_id, name, student_id):
       super().__init__(person_id, name, student_id)

class GraduateStudent(Student):
    def __init__(self, person_id, name, student_id):
       super().__init__(person_id, name, student_id)