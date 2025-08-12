from typing import List


class Solution:
    def get_valid_unique_numbers(self, n: int, x: int):
        num = 1
        res = []
        while num**x <= n:
            res.append(num)
            num += 1
        # print("unique valid nums", res)
        return res

    def helper(self, curr_idx: int, curr_val: int, x: int, unique_numbers: List[int], memo):
        # place this before
        if curr_val == 0:
            return 1

        if curr_val < 0 or curr_idx == len(unique_numbers):
            return 0

        if (curr_idx, curr_val) in memo:
            return memo[(curr_idx, curr_val)]

        pass_val = self.helper(curr_idx=curr_idx + 1, curr_val=curr_val, x=x, unique_numbers=unique_numbers, memo=memo)
        take_val = self.helper(
            curr_idx=curr_idx + 1,
            curr_val=curr_val - (unique_numbers[curr_idx] ** x),
            x=x,
            unique_numbers=unique_numbers,
            memo=memo,
        )
        memo[(curr_idx, curr_val)] = pass_val + take_val

        return memo[(curr_idx, curr_val)]

    def numberOfWays(self, n: int, x: int) -> int:
        memo = {}
        unique_numbers = self.get_valid_unique_numbers(n, x)
        return self.helper(0, n, x, unique_numbers, memo) % (10**9 + 7)


sol = Solution()
print(sol.numberOfWays(213, 1))
"""
We can see we have to find ways to create value n from unique numbers with power of x summed like m1^x + m2^x + m3^x... ma^x = n
For this we have to first understand the limits. The final number 1<=n<=300 and 1<=x<=5
this means we can find first the numbers from 1 to 300 where m^x<=n and since x min is 1 and n max is 300 then m ranges from [1,300]
"""
