import unittest
from karatsuba import karatsuba 

class TestKaratsuba(unittest.TestCase):

    def test_large_numbers(self):
        numberOne = 12345678
        numberTwo = 87654321
        result = karatsuba(numberOne, numberTwo)
        expected = numberOne * numberTwo
        self.assertEqual(result, expected)

    def test_another_large_case(self):
        numberOne = 98765432
        numberTwo = 12345678
        result = karatsuba(numberOne, numberTwo)
        expected = numberOne * numberTwo
        self.assertEqual(result, expected)

    def test_small_numbers(self):
        numberOne = 34
        numberTwo = 56
        result = karatsuba(numberOne, numberTwo)
        expected = numberOne * numberTwo
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
