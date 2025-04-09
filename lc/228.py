from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.sort()
        nums.append(21)
        n = len(nums)
        i = 0
        tmp = []
        res = []
        while i < n:
            if tmp == []:
                tmp.append(nums[i])
                i += 1
            elif tmp[-1] + 1 == nums[i]:
                tmp.append(nums[i])
                i += 1
            else:
                print(tmp)
                string = ""
                if len(tmp) == 1:
                    string = str(tmp[-1])
                    res.append(string)
                else:
                    string = f"{tmp[0]}->{tmp[-1]}"
                    res.append(string)

                tmp = []

        return res


nums = [0, 1, 2, 4, 5, 7]
s = Solution()
print(s.summaryRanges(nums))
