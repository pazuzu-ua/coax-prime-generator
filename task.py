# Prime numbers generator via Sieve of Eratosthenes
# Author: Dmytro Tymoshchenko


def prime_numbers(limit: int) -> int:
    """Generate prime numbers upto *num*."""
    excluded = set()
    for number in range(2, limit+1):
        if number not in excluded:
            yield number
            excluded.update(
                range(number * number, limit+1, number)
            )


if __name__ == '__main__':
    print("Prime numbers upto 1000:", end=" ")
    for el in prime_numbers(1000):
        print(el, end=" ")
