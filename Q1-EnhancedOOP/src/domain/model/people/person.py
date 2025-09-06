# =======================================================
# File: person.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    @abstractmethod
    def get_responsibilities(self):
        pass
