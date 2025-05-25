class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for char in s:
            stack.append(char)
            while len(stack) >= 2:
                a, b = stack[-2], stack[-1]
                diff = abs(ord(a) - ord(b))
                if diff == 1 or diff == 25:
                    stack.pop()
                    stack.pop()
                else:
                    break
        return "".join(stack)


sol = Solution()
print(sol.resultingString("zadb"))
