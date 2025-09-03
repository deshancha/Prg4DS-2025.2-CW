# =======================================================
# File: test_person.py
# Created by: CD
# Date: 2025-09-03
# =======================================================

import unittest

from people.person import Person

class TestPerson(unittest.TestCase):

    def test_person_init_ok(self):
        test_name = "Nimal"
        test_id = 55
        p = Person(test_id, test_name)
        self.assertEqual(p.person_id, test_id)
        self.assertEqual(p.name, test_name)

if __name__ == "__main__":
    unittest.main()