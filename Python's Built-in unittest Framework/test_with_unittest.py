import unittest
from calculator import add_numbers, divide_numbers

class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(10, 20), 30)

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        self.assertEqual(add_numbers(-5, -3), -8)
        self.assertEqual(add_numbers(-10, 5), -5)

    def test_add_with_zero(self):
        """Test adding with zero"""
        self.assertEqual(add_numbers(0, 5), 5)
        self.assertEqual(add_numbers(7, 0), 7)

    def test_divide_normal_cases(self):
        """Test normal division"""
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertEqual(divide_numbers(15, 3), 5)
        self.assertAlmostEqual(divide_numbers(7, 2), 3.5)

    def test_divide_by_zero(self):
        """Test division by zero raises error"""
        with self.assertRaises(ValueError):
            divide_numbers(5, 0)
        
        with self.assertRaises(ValueError):
            divide_numbers(0, 0)

if __name__ == "__main__":
    unittest.main()
