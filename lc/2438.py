from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        prefix_sum = []
        i = 1
        while i <= n:
            if (n & i) != 0:
                prefix_sum.append(i * prefix_sum[-1] if prefix_sum else i)
            i <<= 1

        ans = []
        MOD = 10**9 + 7

        for left, right in queries:
            if left == 0:
                ans.append(prefix_sum[right] % MOD)
            else:
                ans.append((prefix_sum[right] // prefix_sum[left - 1]) % MOD)
        return ans


sol = Solution()
print(sol.productQueries(13, [[1, 2], [1, 1]]))
# print(sol.productQueries(15, [[0, 1], [2, 2], [0, 3]]))
# print(sol.productQueries(2, [[0, 0]]))
# print(sol.productQueries(23, []))
"""
The number n is made of minimum powers of 2 summed to make the array. Example -  9=> [1,8] as 1+8=9
15 => [1,2,4,8] as 1+2+4+8=15

We need to use min numbers to create this array and this is kind of confirmed that such array will always exist

If we represent n as a sum of powers of two, then we just get the binary representation of the number. Each bit in the number represents a unique power of two.

n = 15 = 0b1111

1 = 0b0001
2 = 0b0010
4 = 0b0100
8 = 0b1000

powers = [1,2,4,8]


Reference - https://leetcode.com/problems/range-product-queries-of-powers/solutions/7066145/clear-explanation-i-promise/?envType=daily-question&envId=2025-08-11
"""
