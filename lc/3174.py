class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit() and len(stack):
                stack.pop()
            elif char.isalpha():
                stack.append(char)

        res = ""
        while len(stack):
            res += stack.pop()

        # return reversed string as last element is first
        return res[::-1]


"""
Here we want to see if a digit comes and then remove the closest character on the left of it. We can do it via stack where we pop element when we see the current string
character happens to be a number and if not then add to stack.
We reverse the stack data on combine as it is in reverse order.
"""
