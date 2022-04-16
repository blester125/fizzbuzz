#!/usr/bin/env python3

import functools
import operator as op
import random
import unittest

import fizzbuzz

TRIALS = 100000
PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
]

class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz(self):
        for _ in range(TRIALS):
            num_factors = random.randint(1, len(PRIMES))
            factors = random.choices(PRIMES, k=num_factors)
            number = functools.reduce(op.mul, factors, 1)
            if 3 in factors and 5 in factors:
                gold = "FizzBuzz"
            elif 3 in factors:
                gold = "Fizz"
            elif 5 in factors:
                gold = "Buzz"
            else:
                gold = str(number)

            self.assertEqual(fizzbuzz.fizzbuzz(number), gold)


if __name__ == "__main__":
    unittest.main()
