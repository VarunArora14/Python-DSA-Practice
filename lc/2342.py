from typing import List
import heapq


class Solution:
    def calculateDigits(self, number: int):
        digit_sum = 0
        while number:
            digit_sum += number % 10
            number = number // 10
        return digit_sum

    def maximumSum(self, nums: List[int]) -> int:
        mapper = dict()
        for num in nums:
            digit_sum = self.calculateDigits(num)
            if digit_sum not in mapper:
                mapper[digit_sum] = []
                heapq.heappush(mapper[digit_sum], num)
            elif len(mapper[digit_sum]) == 2:
                heapq.heappush(mapper[digit_sum], num)
                heapq.heappop(mapper[digit_sum])  # remove the smallest element as min heap
            else:
                heapq.heappush(mapper[digit_sum], num)
            # print(num, mapper[digit_sum], digit_sum)

        max_sum = -1
        # print(mapper)
        for digit_sum, q in mapper.items():
            if len(q) == 2:
                max_sum = max(max_sum, q[0] + q[1])

        return max_sum


s = Solution()
print(s.maximumSum(nums=[10, 12, 19, 14]))

"""
for each number, we calculate the sum of digits and then map to it two values. If mapper[count] has less than 2 elements then simply add the numbers and if it has 2 then - 
make a heap or array sorted to store the values of the largest 2 elements in the list. 

While we use heap, the space complexity O(n) where for n unique digit sum, we have n different constant sized heaps.

Time complexity - 
For each run, we first find the digit sum taking log10n time where n is the number (log10 n operations to go from n to 0) and since this is processed for m numbers then total time complexity for worst case scenario is O(m logn)

Space Complexity - The heaps store 2 elements at max so their space and time complexity of operations become constant.
The size of map is based on the digit sum which for a number can have O(log10 n) time complexity and this is multiplied by number of elements in heap (2) making this O(log10 n)*2 = O(log10 n) as space complexity
"""
