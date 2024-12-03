import unittest
from day2 import is_safe, count_safe_reports, count_safe_dampened_reports

class TestDay2(unittest.TestCase):
    def test_is_safe(self):
        self.assertTrue(is_safe([1, 2, 3]))
        self.assertTrue(is_safe([3, 2, 1]))
        self.assertFalse(is_safe([1, 3, 2, 4, 5]))
        self.assertTrue(is_safe([7, 6, 4, 2, 1]))
        
        self.assertTrue(is_safe([1, 3, 6, 7, 9]))
        # 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
        self.assertTrue(is_safe([7, 6, 4, 2, 1]))
        # 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
        self.assertFalse(is_safe([1, 2, 7, 8, 9]))
        # 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
        self.assertFalse(is_safe([9, 7, 6, 2, 1]))
        # 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
        self.assertFalse(is_safe([1, 3, 2, 4, 5]))
        # 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
        self.assertFalse(is_safe([8, 6, 4, 4, 1]))
        # 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
        self.assertTrue(is_safe([1, 3, 6, 7, 9]))


    def test_count_safe_reports(self):
        lines = [
            "7 6 4 2 1\n",
            "1 2 7 8 9\n",
            "9 7 6 2 1\n",
            "1 3 2 4 5\n",
            "8 6 4 4 1\n",
            "1 3 6 7 9\n"
        ]
        safe_reports = count_safe_reports(lines)
        self.assertEqual(safe_reports, 2)

    def test_count_safe_dampened_reports(self):
        lines = [
            "7 6 4 2 1\n",
            "1 2 7 8 9\n",
            "9 7 6 2 1\n",
            "1 3 2 4 5\n",
            "8 6 4 4 1\n",
            "1 3 6 7 9\n"
        ]
        safe_dampened_reports = count_safe_dampened_reports(lines)
        self.assertEqual(safe_dampened_reports, 4)

if __name__ == '__main__':
    unittest.main()