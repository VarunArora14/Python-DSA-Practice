from typing import List


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True


class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        primes = set()
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                substr = s[i : j + 1]
                stripped = substr.lstrip("0")
                if not stripped:
                    num = 0
                else:
                    num = int(stripped)
                if num >= 2 and is_prime(num):
                    primes.add(num)
        sorted_primes = sorted(primes, reverse=True)
        if len(sorted_primes) == 0:
            return 0
        elif len(sorted_primes) <= 3:
            return sum(sorted_primes)
        else:
            return sum(sorted_primes[:3])


sol = Solution()
print(sol.sumOfLargestPrimes("12234"))
