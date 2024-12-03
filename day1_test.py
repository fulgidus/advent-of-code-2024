
import unittest
from day1 import calculate_distance_and_similarity

class TestDay1(unittest.TestCase):
    def test_calculate_distance_and_similarity(self):
        with open('day1.txt', 'r') as file:
            lines = file.readlines()
            distance, similarity = calculate_distance_and_similarity(lines)
            self.assertEqual(distance, 2285373)
            self.assertEqual(similarity, 21142653)

if __name__ == '__main__':
    unittest.main()