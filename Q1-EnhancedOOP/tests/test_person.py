# =======================================================
# File: test_person.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

import unittest

from domain.model.people.person import Person

# file private DummyPerson for suport testing abstract Person
class _DummyPerson(Person):
    def get_responsibilities(self):
        return super().about()

class TestPerson(unittest.TestCase):
    def test_person_init_ok(self):
        test_name = "Nimal"
        test_id = 55
        person = _DummyPerson(test_id, test_name)
        self.assertEqual(person.person_id, test_id)
        self.assertEqual(person.name, test_name)

if __name__ == "__main__":
    unittest.main()