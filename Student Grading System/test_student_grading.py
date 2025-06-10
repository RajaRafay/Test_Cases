import unittest
from student_grading import get_grade

class gradeTesting(unittest.TestCase):
    def test_studentGradeGreaterThan100(self):
        self.assertEqual(get_grade(101),'No grade above 100')
        self.assertEqual(get_grade(-4),'No grade below 0')
        self.assertEqual(get_grade(88),'B')

if __name__ == "__main__":
    unittest.main()