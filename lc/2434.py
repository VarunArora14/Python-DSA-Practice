class Solution:
    def robotWithString(self, s: str) -> str:
        mapper = {}
        for idx, char in enumerate(s):
            if char not in mapper:
                mapper[char] = []
            mapper[char].append(idx)
