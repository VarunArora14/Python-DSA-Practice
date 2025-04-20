from typing import List


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)

        visited = set()
        i = 0
        score = 0

        while 0 <= i < n:
            if i in visited:
                break
            visited.add(i)

            if instructions[i] == "add":
                score += values[i]
                i += 1
            else:
                i += values[i]

        return score


sol = Solution()
instructions = ["jump", "add", "add"]
values = [3, 1, 1]
print(sol.calculateScore(instructions, values))
