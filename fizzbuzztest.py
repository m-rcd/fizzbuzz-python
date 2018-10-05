import unittest
from fizzbuzz import *

class Tests(unittest.TestCase):
    def test_IsDivisibleBy3(self):
        self.assertEqual(IsDivisibleByNumber(3, 3), True)

    def test_IsNotDivisibleBy3(self):
        self.assertEqual(IsDivisibleByNumber(1, 3), False)

    def test_IsDivisibleBy5(self):
        self.assertEqual(IsDivisibleByNumber(5, 5), True)

    def test_IsNotDivisibleBy5(self):
        self.assertEqual(IsDivisibleByNumber(1, 5), False)

    def test_IsDivisibleBy15(self):
        self.assertEqual(IsDivisibleByNumber(15, 15), True)

    def test_IsNotDivisibleBy15(self):
        self.assertEqual(IsDivisibleByNumber(1, 15), False)

    def test_fizzbuzzsaysfizz(self):
        self.assertEqual(FizzbuzzSays(3), 'fizz')

    def test_fizzbuzzsaysbuzz(self):
        self.assertEqual(FizzbuzzSays(5), 'buzz')

    def test_fizzbuzzsaysfizzbuzz(self):
        self.assertEqual(FizzbuzzSays(15), 'fizzbuzz')

    def test_returnnumber(self):
        self.assertEqual(FizzbuzzSays(4), 4)
unittest.main()
