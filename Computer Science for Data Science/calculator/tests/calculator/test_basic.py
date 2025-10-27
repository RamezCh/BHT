import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.calculator import Calculator


class TestCalculatorFactorize(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Regular cases
    def test_regular_cases(self):
        # n = 1
        self.assertEqual(self.calc.factorize(1), [])

        # n = 2 (prime)
        self.assertEqual(self.calc.factorize(2), [2])

        # n = 3 (prime)
        self.assertEqual(self.calc.factorize(3), [3])

        # n = 4 (2^2)
        self.assertEqual(self.calc.factorize(4), [2, 2])

        # n = 27 (3^3)
        self.assertEqual(self.calc.factorize(27), [3, 3, 3])

        # n = 65536 (2^16)
        self.assertEqual(self.calc.factorize(65536), [2] * 16)

        # n = 100000039 (prime number)
        self.assertEqual(self.calc.factorize(100000039), [100000039])

    def test_regular_case_10952347(self):
        # n = 10952347 - test that factors multiply to original number
        result = self.calc.factorize(10952347)
        product = 1
        for factor in result:
            product *= factor
        self.assertEqual(product, 10952347)

    # Corner cases (valid)
    def test_corner_cases(self):
        # n = 0
        self.assertEqual(self.calc.factorize(0), [])

        # n = 2147483646 (MAX_INT-1)
        # 2147483646 = 2 * 3 * 3 * 7 * 11 * 31 * 151 * 331
        expected = [2, 3, 3, 7, 11, 31, 151, 331]
        self.assertEqual(self.calc.factorize(2147483646), expected)

        # n = 2147483647 (MAX_INT) - prime number
        self.assertEqual(self.calc.factorize(2147483647), [2147483647])

    # Error and exception cases (invalid)
    def test_negative_numbers_raise_exception(self):
        test_cases = [-1, -10, -2147483648]

        for n in test_cases:
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    self.calc.factorize(n)

    def test_float_numbers_raise_exception(self):
        # Test that non-integer floats raise ValueError
        test_cases = [2.5, 3.14, 10.7]

        for n in test_cases:
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    self.calc.factorize(n)

    def test_integer_floats_work(self):
        # Test that integer floats work correctly
        self.assertEqual(self.calc.factorize(4.0), [2, 2])
        self.assertEqual(self.calc.factorize(27.0), [3, 3, 3])

    # Test with different input formats (using your _parse_input capabilities)
    def test_english_number_words(self):
        self.assertEqual(self.calc.factorize("four"), [2, 2])
        self.assertEqual(self.calc.factorize("seven"), [7])
        self.assertEqual(self.calc.factorize("FOUR"), [2, 2])  # case insensitive
        self.assertEqual(self.calc.factorize("Four"), [2, 2])  # mixed case

    def test_german_number_words(self):
        self.assertEqual(self.calc.factorize("vier"), [2, 2])
        self.assertEqual(self.calc.factorize("sieben"), [7])

    def test_spanish_number_words(self):
        self.assertEqual(self.calc.factorize("cuatro"), [2, 2])
        self.assertEqual(self.calc.factorize("siete"), [7])

    def test_russian_number_words(self):
        self.assertEqual(self.calc.factorize("четыре"), [2, 2])
        self.assertEqual(self.calc.factorize("семь"), [7])

    def test_chinese_number_words(self):
        self.assertEqual(self.calc.factorize("四"), [2, 2])
        self.assertEqual(self.calc.factorize("七"), [7])

    def test_latin_numerals(self):
        self.assertEqual(self.calc.factorize("iv"), [2, 2])
        self.assertEqual(self.calc.factorize("VII"), [7])  # case insensitive

    def test_roman_numerals_basic(self):
        self.assertEqual(self.calc.factorize("IV"), [2, 2])
        self.assertEqual(self.calc.factorize("X"), [2, 5])  # 10 = 2 * 5

    # Additional test to verify factorization correctness
    def verify_factorization(self, n, factors):
        if n <= 1:
            self.assertEqual(factors, [])
            return

        product = 1
        for factor in factors:
            product *= factor
            # Verify each factor is prime (basic check)
            self.assertGreater(factor, 1)

        self.assertEqual(product, n)

    def test_factorization_correctness(self):
        test_cases = [2, 3, 4, 27, 65536, 100000039, 2147483646, 2147483647]

        for n in test_cases:
            with self.subTest(n=n):
                factors = self.calc.factorize(n)
                self.verify_factorization(n, factors)

    # Test edge cases for _parse_input integration
    def test_string_numbers(self):
        self.assertEqual(self.calc.factorize("4"), [2, 2])
        self.assertEqual(self.calc.factorize("27"), [3, 3, 3])

    def test_invalid_inputs(self):
        invalid_inputs = ["hello", "abc", "eleven", ""]

        for invalid_input in invalid_inputs:
            with self.subTest(input=invalid_input):
                with self.assertRaises(ValueError):
                    self.calc.factorize(invalid_input)

    # Test prime numbers specifically
    def test_prime_numbers(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for prime in primes:
            with self.subTest(prime=prime):
                self.assertEqual(self.calc.factorize(prime), [prime])

    # Test composite numbers
    def test_composite_numbers(self):
        test_cases = [
            (6, [2, 3]),
            (8, [2, 2, 2]),
            (12, [2, 2, 3]),
            (15, [3, 5]),
            (18, [2, 3, 3]),
            (25, [5, 5]),
            (30, [2, 3, 5])
        ]

        for number, expected_factors in test_cases:
            with self.subTest(number=number):
                self.assertEqual(self.calc.factorize(number), expected_factors)


class TestCalculatorOtherOperations(unittest.TestCase):
    """Test other calculator operations to ensure they still work"""

    def setUp(self):
        self.calc = Calculator()

    def test_add_operation(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add("two", "three"), 5)

    def test_sub_operation(self):
        self.assertEqual(self.calc.sub(5, 3), 2)
        self.assertEqual(self.calc.sub("five", "three"), 2)

    def test_mul_operation(self):
        self.assertEqual(self.calc.mul(2, 3), 6)
        self.assertEqual(self.calc.mul("two", "three"), 6)

    def test_div_operation(self):
        self.assertEqual(self.calc.div(6, 3), 2)
        self.assertEqual(self.calc.div("six", "three"), 2)


if __name__ == '__main__':
    unittest.main()