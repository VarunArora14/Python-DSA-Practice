from typing import List


class Solution:
    def minSumOptimized(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        zeros1, zeros2 = nums1.count(0), nums2.count(0)
        sum1 += zeros1
        sum2 += zeros2

        if (zeros1 == 0 and sum2 > sum1) or (zeros2 == 0 and sum1 > sum2):
            return -1

        return max(sum1, sum2)

    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1_zero_count = nums1.count(0)
        n2_zero_count = nums2.count(0)

        n1_sum = sum(nums1)
        n2_sum = sum(nums2)

        is_n1_bigger = True if n1_sum + n1_zero_count > n2_sum + n2_zero_count else False

        if is_n1_bigger:
            diff = n1_sum + n1_zero_count - n2_sum

            if n2_zero_count == 0 and diff != 0:
                return -1

            if n2_zero_count > diff:
                return -1
            else:
                return n1_sum + n1_zero_count
        else:
            diff = n2_sum + n2_zero_count - n1_sum

            if diff != 0 and n1_zero_count == 0:
                return -1

            if diff < n1_zero_count:
                return -1
            return n2_sum + n2_zero_count


sol = Solution()
nums1 = [3, 2, 0, 1, 0]
nums2 = [6, 5, 0]
print(sol.minSum(nums1=nums1, nums2=nums2))

nums1 = [2, 0, 2, 0]
nums2 = [1, 4]
print(sol.minSum(nums1=nums1, nums2=nums2))

nums1 = [8, 13, 15, 18, 0, 18, 0, 0, 5, 20, 12, 27, 3, 14, 22, 0]
nums2 = [29, 1, 6, 0, 10, 24, 27, 17, 14, 13, 2, 19, 2, 11]
print(sol.minSum(nums1, nums2))

"""
We can perform the operations only when there are 0's possible on side with smaller value to match upto larger value.
If both the sums are unequal and 0 count of smaller is 0, it cannot reach that value. For the larger value, we replace the 0's with 1
"""
