class Solution:
    def solve(self, n):
        print("hey", n)
        # base case of no node or single node as left/right subtree
        if n <= 1:
            return 1
        ans = 0

        # start from 1 to
        for i in range(1, n + 1):
            left_combinations = self.solve(i - 1)  # for remaining numbers of left subtree
            right_combinations = self.solve(n - i)

            ans += left_combinations * right_combinations
        return ans

    def dp_solution(self, n):
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        # dp[x] means that for x number of nodes, there are dp[x] possible BSTs and we use this number for overlapping subproblems

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]

    def numTrees(self, n: int) -> int:
        return self.dp_solution(n)


s = Solution()
n = 3
print(s.numTrees(n))
