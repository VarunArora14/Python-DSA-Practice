class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = right = total = 0
        # Track frequency of a, b, c
        freq = [0] * 3

        while right < len(s):
            # Add character at right pointer to frequency array
            freq[ord(s[right]) - ord("a")] += 1

            # While we have all required characters
            while self._has_all_chars(freq):
                # All substrings from current window to end are valid
                # Add count of valid substrings
                total += len(s) - right

                # Remove leftmost character and move left pointer
                freq[ord(s[left]) - ord("a")] -= 1
                left += 1

            right += 1

        return total

    def _has_all_chars(self, freq: list) -> bool:
        # Check if we have at least one of each character
        return all(f > 0 for f in freq)


s = Solution()
"""
The solution should follow more like a sliding window as once we find window with 'a', 'b' and 'c', we do constant operation to find the remaining substrings. So, we can
optimise the solution to have single traversal.
This would be optimisation of brute force approach of finding the substrings and then checking 'a', 'b' and 'c' in it.


"""
