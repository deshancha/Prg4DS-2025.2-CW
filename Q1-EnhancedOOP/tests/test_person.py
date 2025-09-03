# =======================================================
# File: test_person.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

import unittest

from people.person import Person

# file private DummyPerson for suport testing abstract Person
class _DummyPerson(Person):
    def about(self):
        return super().about()

class TestPerson(unittest.TestCase):
    def test_person_init_ok(self):
        test_name = "Nimal"
        test_id = 55
        p = _DummyPerson(test_id, test_name)
        self.assertEqual(p.person_id, test_id)
        self.assertEqual(p.name, test_name)

if __name__ == "__main__":
    unittest.main()