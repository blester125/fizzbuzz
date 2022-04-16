#!/usr/bin/env python3

import functools


def _fizzbuzz(n: int) -> str:
    def test(div: int, string: str, f):
        if n % div == 0:
            return lambda _: string + f("")
        return f

    fizz = functools.partial(test, 3, "Fizz")
    buzz = functools.partial(test, 5, "Buzz")
    id_ = lambda s: s
    return fizz(buzz(id_))(str(n))

def fizzbuzz(n: int):
    for i in range(1, n + 1):
        print(_fizzbuzz(i))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="FizzBuzz with no extra work.")
    parser.add_argument("n", type=int, help="The number to fizzbuzz to.")
    args = parser.parse_args()

    fizzbuzz(args.n)
