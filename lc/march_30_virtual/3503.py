class Solution:
    def __init__(self):
        self.substr_first_set = set()
        self.substr_second_set = set()

    def generate_substrings(self, s: str, t: str):
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                self.substr_first_set.add(s[i : j + 1])

        for i in range(len(t)):
            for j in range(i, len(t)):
                self.substr_second_set.add(t[i : j + 1])

    def is_palindrome(self, string):
        if len(string) <= 1:
            return True

        i = 0
        j = len(string) - 1
        while i <= j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1

        return True

    def longestPalindrome(self, s: str, t: str) -> int:
        self.generate_substrings(s, t)
        max_len = 1
        self.substr_first_set.add("")
        self.substr_second_set.add("")
        # print(self.substr_second_set)
        for x in self.substr_first_set:
            for y in self.substr_second_set:
                if self.is_palindrome(x + y):
                    # print(x + y)
                    max_len = max(max_len, len(x + y))

        return max_len


sol = Solution()
s = "f"
t = "zzvz"
print(sol.longestPalindrome(s, t))
