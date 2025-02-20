from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        binary_num_strs = set()
        for i in range(0, 17):
            binary_num_strs.add(i)  # get only the binary

        for num_str in nums:
            curr_num = int(num_str, 2)
            if curr_num in binary_num_strs:
                binary_num_strs.remove(curr_num)

        res = bin(binary_num_strs.pop())[2:]
        print("res", res)
        len_diff = n - len(res)
        return "0" * len_diff + res


s = Solution()
nums = ["1"]
print(s.findDifferentBinaryString(nums=nums))
