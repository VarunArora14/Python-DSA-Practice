from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        st = set()
        for a in arr:
            st.add(a)

        max_len = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                curr_len = 2
                f = arr[i]
                s = arr[j]
                while f + s in st:
                    t = f
                    f = s
                    s = t + s
                    curr_len += 1
                    max_len = max(max_len, curr_len)
        return max_len


s = Solution()
arr = [1, 3, 7, 11, 12, 14, 18]
print(s.lenLongestFibSubseq(arr=arr))
