from typing import List


class Solution:
    def _check_all_chars_present(self, freq_arr: List[int]):
        return all([f > 0 for f in freq_arr])
        # returns True only when all elements of this array is True for condition inside

    def numberOfSubstrings(self, s: str) -> int:
        start, end = 0, 0
        freqs_arr = [0, 0, 0]
        res = 0
        while end < len(s):
            freqs_arr[ord(s[end]) - ord("a")] += 1

            while self._check_all_chars_present(freq_arr=freqs_arr):
                res += len(s) - end  # remaining indices + current substr count

                freqs_arr[ord(s[start]) - ord("a")] -= 1  # we move start forward to slide window
                start += 1

            end += 1  # move end of window forward (IMP)

        return res


s = Solution()
print(s.numberOfSubstrings("abcabc"))
"""
The solution should follow more like a sliding window as once we find window with 'a', 'b' and 'c', we do constant operation to find the remaining substrings. So, we can
optimise the solution to have single traversal.
This would be optimisation of brute force approach of finding the substrings and then checking 'a', 'b' and 'c' in it.


"""
