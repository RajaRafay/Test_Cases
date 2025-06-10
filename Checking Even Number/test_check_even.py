import unittest
from check_even import is_even

class gradeTesting(unittest.TestCase):
    def test_studentGradeGreaterThan100(self):
        self.assertEqual(is_even(4),True)
        self.assertEqual(is_even(3),False)
        self.assertEqual(is_even(""),'No number exists')
        self.assertEqual(is_even(-6),'Negative number')

if __name__ == "__main__":
    unittest.main()