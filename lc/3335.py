from functools import cache


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        @cache
        def helper(s, t):
            ans = 0
            for c in s:
                if ord(c) + t <= ord("z"):
                    ans += 1
                else:
                    new_t = t
                    new_t -= ord("z") + 1 - ord(c)
                    ans += helper("ab", new_t)
            return ans

        return helper(s, t) % ((10**9) + 7)


s = "abcyy"
t = 2

sol = Solution()
print(sol.lengthAfterTransformations(s, t))

"""
Consider single character operations first - 

'x' -> t=59
x -> z t=58
ab -> 57
yz -> 23
zab -> 22
abbc -> 21


We do caching so that for each character we solve the overlapping problem using memoization where if helper(s,t) as been solved before, it uses
the existing solution and not re-compute it.

We just implement the logic of handling each character in string s where if ord(character) + t >= ord("z") then we recursively call the method
ans += helper("ab", new_t) where new_t is set based on ord(c) value to take it to z first and then +1 step to make it "ab".

We see the overlapping problem that if helper("z", 2) is solved once, it can occur again and has the same solution each time. We store these solutions
via @cache decorator and this optimized the initial recursive method.
"""
