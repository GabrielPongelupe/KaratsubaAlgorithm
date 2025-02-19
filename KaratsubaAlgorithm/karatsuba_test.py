import unittest
from karatsuba import karatsuba 

class TestKaratsuba(unittest.TestCase):

    def test_large_numbers(self):
        """Testa números grandes para garantir que o algoritmo funcione corretamente."""
        number_one = 1234567890123456
        number_two = 9876543210987654
        result = karatsuba(number_one, number_two)
        expected = number_one * number_two
        self.assertEqual(result, expected)

    def test_another_large_case(self):
        """Testa outro conjunto de números grandes."""
        number_one = 9876543211234567
        number_two = 1928374655647382
        result = karatsuba(number_one, number_two)
        expected = number_one * number_two
        self.assertEqual(result, expected)

    def test_small_numbers(self):
        """Testa números pequenos para verificar a base do algoritmo."""
        number_one = 12
        number_two = 34
        result = karatsuba(number_one, number_two)
        expected = number_one * number_two
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        """Testa números negativos para validar comportamento com sinais."""
        number_one = -1234
        number_two = 5678
        result = karatsuba(number_one, number_two)
        expected = number_one * number_two
        self.assertEqual(result, expected)

        number_one = -1234
        number_two = -5678
        result = karatsuba(number_one, number_two)
        expected = number_one * number_two
        self.assertEqual(result, expected)

    def test_multiplication_by_zero(self):
        """Testa multiplicação por zero."""
        self.assertEqual(karatsuba(0, 123456), 0)
        self.assertEqual(karatsuba(7891011, 0), 0)
        self.assertEqual(karatsuba(0, 0), 0)

    def test_odd_length_numbers(self):
        """Testa números com quantidade ímpar de dígitos."""
        number_one = 12345
        number_two = 67891
        result = karatsuba(number_one, number_two)
        expected = number_one * number_two
        self.assertEqual(result, expected)

    def test_even_length_numbers(self):
        """Testa números com quantidade par de dígitos."""
        number_one = 24680
        number_two = 13579
        result = karatsuba(number_one, number_two)
        expected = number_one * number_two
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
