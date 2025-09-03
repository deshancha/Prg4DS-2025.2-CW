# =======================================================
# File: person.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def about(self):
        return f"ID: {self.person_id}, Name: {self.name}"
