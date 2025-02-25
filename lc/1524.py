from typing import List


class Solution:
    def numOfSubarrays(self, arr):
        MOD = 1000000007
        odd_count, even_count, prefix_sum, result = 0, 1, 0, 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                result = (result + odd_count) % MOD
                even_count += 1
            else:
                result = (result + even_count) % MOD
                odd_count += 1

        return result

    def numOfSubarraysBruteForce(self, arr: List[int]) -> int:
        MOD = 1e9 + 7
        n = len(arr)
        count = 0

        # Generate all possible subarrays
        for start_index in range(n):
            current_sum = 0
            # Iterate through each subarray starting at start_index
            for end_index in range(start_index, n):
                current_sum += arr[end_index]
                # Check if the sum is odd
                if current_sum % 2 != 0:
                    print(arr[start_index : end_index + 1])
                    count += 1

        return int(count % MOD)


s = Solution()
print(s.numOfSubarraysBruteForce([2, 1, 4, 6, 8, 3]))

"""
Here subarray means it can be any
"""
