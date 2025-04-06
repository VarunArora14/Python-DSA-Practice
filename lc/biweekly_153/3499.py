class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        if s.count("1") == 0:
            return 0
        n = len(s)
        max_val = 0
        start_ones, end_ones = -1, -1
        for i, char in enumerate(s):
            if s[i] == "0":
                j = i + 1
                counter = 0
                start = j
                while j < n and s[j] == "1":
                    print("hey")
                    counter += 1
                    j += 1

                if counter > max_val:
                    max_val = counter
                    start_ones = start
                    end_ones = j  # note +1 for iteration
                    print(start_ones, end_ones)

        print(start_ones, end_ones)
        if start_ones == -1 or end_ones == -1:
            return s.count("1")
        if start_ones == 0 or end_ones == len(s):
            return end_ones - start_ones

        for idx in range(start_ones, end_ones):
            s = list(s)  # convert to list
            s[idx] = "0"  # set to 0 for first operation
            s = "".join(s)  # convert back to string

        s = "1" + s + "1"  # augment
        print("after augment:", s)

        start_zeroes, end_zeroes = -1, -1
        for i, char in enumerate(s):
            if s[i] == "1":
                j = i + 1
                counter = 0
                start = j
                while j < n and s[j] == "0":
                    counter += 1
                    j += 1

                if counter > max_val:
                    max_val = counter
                    start_zeroes = start
                    end_zeroes = j  # note +1 for iteration
                    print(start_zeroes, end_zeroes)

        # convert these 0's to 1's
        for idx in range(start_zeroes, end_zeroes + 1):
            s = list(s)  # convert to list
            s[idx] = "1"  # set to 0 for first operation
            s = "".join(s)  # convert back to string

        print(s)
        return s.count("1") - 2


s = Solution()
# string = input()
print(s.maxActiveSectionsAfterTrade("101"))


"""
Two steps - 

1. find most number of 1's between 0's as left and right bound and then convert them to 0's
2. find the largest substring of 0's and make them all 1's
3. return these 1's excluding the augmented 1's
"""
