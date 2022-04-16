#!/usr/bin/env python3

import functools
from typing import Callable


def _test(n: int, d: int, s: str, f: Callable[..., str]) -> Callable[..., str]:
    if n % d == 0:
        return lambda _: s + f("")
    return f


def fizzbuzz(n: int) -> str:
    fizz = functools.partial(_test, n, 3, "Fizz")
    buzz = functools.partial(_test, n, 5, "Buzz")
    return fizz(buzz(lambda s: s))(str(n))


def run(check: Callable[[int], str], n: int):
    for i in range(1, n + 1):
        print(check(i))


def fizzbuzzhisshowl(n: int) -> str:
    fizz = functools.partial(_test, n, 3, "Fizz")
    buzz = functools.partial(_test, n, 5, "Buzz")
    hiss = functools.partial(_test, n, 7, "Hiss")
    howl = functools.partial(_test, n, 9, "Howl")
    return fizz(buzz(hiss(howl(lambda s: s))))(str(n))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="FizzBuzz with no extra work.")
    parser.add_argument("n", type=int, help="The number to fizzbuzz to.")
    parser.add_argument(
        "--hiss-howl", action="store_true",
        help="Should we add Hiss (divisible by 7) and Howl (divisble by 9)?")
    args = parser.parse_args()

    if args.hiss_howl:
      run(fizzbuzzhisshowl, args.n)
    else:
      run(fizzbuzz, args.n)
