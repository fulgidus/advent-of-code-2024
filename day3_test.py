
import unittest
from day3 import process_instructions, extract_and_multiply, extract_and_multiply_all

class TestDay3(unittest.TestCase):

    def test_process_instructions(self):
        self.assertEqual(process_instructions("do() mul(2,3) don't() mul(3,4) do() mul(1,1)"), 7)
        self.assertEqual(process_instructions("mul(2,3) don't() mul(3,4) do() mul(1,1)"), 7)
        self.assertEqual(process_instructions("don't() mul(2,3) do() mul(3,4)"), 12)
        self.assertEqual(process_instructions("do() mul(2,3) do() mul(3,4)"), 18)
        self.assertEqual(process_instructions("mul(2,3) mul(3,4)"), 18)

    def test_extract_and_multiply(self):
        self.assertEqual(extract_and_multiply("do() mul(2,3) don't() mul(3,4) do() mul(1,1)"), 7)
        self.assertEqual(extract_and_multiply("mul(2,3) don't() mul(3,4) do() mul(1,1)"), 7)
        self.assertEqual(extract_and_multiply("don't() mul(2,3) do() mul(3,4)"), 12)
        self.assertEqual(extract_and_multiply("do() mul(2,3) do() mul(3,4)"), 18)
        self.assertEqual(extract_and_multiply("mul(2,3) mul(3,4)"), 18)

    def test_extract_and_multiply_all(self):
        self.assertEqual(extract_and_multiply_all("mul(2,3) mul(3,4)"), 18)
        self.assertEqual(extract_and_multiply_all("mul(1,1) mul(2,2)"), 5)
        self.assertEqual(extract_and_multiply_all("mul(0,1) mul(1,0)"), 0)
        self.assertEqual(extract_and_multiply_all("mul(5,5)"), 25)
        self.assertEqual(extract_and_multiply_all(""), 0)

if __name__ == '__main__':
    unittest.main()