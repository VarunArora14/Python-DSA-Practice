class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = len(s)
        st = set()
        counter = 1
        st.add(s[0])
        for i in range(1, end):
            if s[i] in st:
                # print(s[i])
                while start < i and s[i] in st:
                    st.remove(s[start])
                    start += 1

                # don't remove s[start] once we find and rather go to next character as the s[i] same as s[start]
            st.add(s[i])

            # print(f"Now: i: {i}, start: {start}")
            counter = max(counter, i - start + 1)
        return counter


string = input()
s = Solution()
print(s.lengthOfLongestSubstring(string))
