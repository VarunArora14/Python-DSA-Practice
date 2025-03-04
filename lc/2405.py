class Solution:
    def partitionString(self, s: str) -> int:
        curr_substr_set = set()
        substr_count = 1
        for i in range(len(s)):
            if s[i] in curr_substr_set:
                substr_count += 1
                curr_substr_set = set([s[i]])
            else:
                curr_substr_set.add(s[i])

        return substr_count


s = Solution()
print(s.partitionString("ssssss"))
