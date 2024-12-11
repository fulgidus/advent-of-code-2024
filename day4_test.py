
import unittest
from day4 import count_XMAS, count_xmas_trees, read_input_from_file

class TestDay4(unittest.TestCase):
    def test_count_xmas_normal(self):
        grid = [
            "XMASX",
            "AXMAX",
            "XMAXS",
            "AMXAS",
            "SAXMA"
        ]
        result = count_XMAS(grid)
        self.assertEqual(result, 1)

    def test_count_xmas_trees_normal(self):
        matrix = [
            ['X', 'A', 'M', 'X'],
            ['M', 'M', 'M', 'A'],
            ['A', 'A', 'S', 'M'],
            ['S', 'A', 'M', 'S']
        ]
        rows, cols = 4, 4
        result = count_xmas_trees(matrix, rows, cols)
        self.assertEqual(result, 0)

    def test_read_input_from_file(self):
        test_file_path = 'day4.txt'
        with open(test_file_path, 'w') as f:
            f.write('XMAS\nAMAS\nXMAS\nXMAS')
        grid, rows, cols = read_input_from_file(test_file_path)
        self.assertEqual(rows, 4)
        self.assertEqual(cols, 4)
        self.assertEqual(grid, ['XMAS', 'AMAS', 'XMAS', 'XMAS'])

if __name__ == '__main__':
    unittest.main()