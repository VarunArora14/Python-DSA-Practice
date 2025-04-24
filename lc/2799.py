class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        distinct_count = len(set(nums))

        n = len(nums)
        start = 0
        res = 0
        mapper = {}
        for end in range(n):
            if nums[end] not in mapper:
                mapper[nums[end]] = 0
            mapper[nums[end]] += 1
            while len(mapper.keys()) == distinct_count:
                res += n - end  # all remaining on right subarrays must be included with current
                print(start, nums[start : end + 1])
                mapper[nums[start]] -= 1
                if mapper[nums[start]] == 0:
                    del mapper[nums[start]]
                start += 1  # make window smaller

        return res


sol = Solution()
nums = [1, 3, 1, 2, 2]
print(sol.countCompleteSubarrays(nums))
