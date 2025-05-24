from bisect import bisect_left


class Solution:
    def maxSubstrings(self, word: str) -> int:
        pos = {}
        for i, ch in enumerate(word):
            if ch not in pos:
                pos[ch] = []
            pos[ch].append(i)

        intervals = []
        for ch, P in pos.items():
            m = len(P)
            for k in range(m):
                needed = P[k] + 3
                ele = bisect_left(P, needed, lo=k + 1)
                if ele < m:
                    intervals.append((P[k], P[ele]))

        intervals.sort(key=lambda x: x[1])
        count = 0
        last_end = -1
        for start, end in intervals:
            if start > last_end:
                count += 1
                last_end = end

        return count


sol = Solution()
print(sol.maxSubstrings("bcdaaaab"))
