from typing import Counter
from heapq import heappop, heappush, heapify

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        n, hp = 0, []
        for c in sorted(cnt, reverse=True):
            heappush(hp, (n, c))
            n += 1
        ans = ""
        while hp:
            if cnt[hp[0][1]] <= repeatLimit:    # use all
                n1, c1 = heappop(hp)
                ans += c1 * cnt[c1]
            else:                               # use the limited number
                n1, c1 = heappop(hp)
                ans += c1 * repeatLimit
                cnt[c1] -= repeatLimit
                if hp:                          # use 1 of the next character
                    n2, c2 = heappop(hp)
                    ans += c2
                    cnt[c2] -= 1
                    if cnt[c2]:
                        heappush(hp, (n2, c2))  # push the next character back
                    heappush(hp, (n1, c1))      # push the current character back
        return ans
            
s=Solution()
print(s.repeatLimitedString(s="cczazcc", repeatLimit=3))