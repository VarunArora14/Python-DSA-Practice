from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()

        # make sure number does not start with 0 and same idx does not repeat
        n = len(digits)
        res = []
        s = set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k and digits[i] != 0 and digits[k] % 2 == 0:
                        val = 100 * digits[i] + 10 * digits[j] + digits[k]
                        if val not in s:
                            res.append(val)
                            s.add(val)

        return res


sol = Solution()

digits = [2, 1, 3, 0]
digits = [2, 2, 8, 8, 2]
print(sol.findEvenNumbers(digits=digits))

"""
Checks - 

- indices i,j,k must not be same
- first digit not 0
- last digit digits[k]%2==0 
- val must not repeat in answer
"""
