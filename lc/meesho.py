def getMaximumSum(no_adjacent, one_adjacent, both_adjacent):
    n = len(no_adjacent)
    dp = [0] * n  # DP array to store the max sum for each deployment step

    # First processor has no adjacent deployed
    dp[0] = no_adjacent[0]
    
    if n > 1:
        # Second processor can either:
        # - Be deployed second with only the first one deployed
        dp[1] = max(no_adjacent[1], dp[0] + one_adjacent[1])
    
    # Fill DP table for remaining processors
    for i in range(2, n):
        # Case 1: Deploy `i` first → Take `no_adjacent[i]`
        option1 = dp[i-1] + no_adjacent[i]

        # Case 2: Deploy `i` when one adjacent is deployed → Take `one_adjacent[i]`
        option2 = dp[i-2] + one_adjacent[i]

        # Case 3: Deploy `i` when both adjacent are deployed → Take `both_adjacent[i]`
        option3 = dp[i-3] + both_adjacent[i] if i >= 3 else 0

        # Take the best option
        dp[i] = max(option1, option2, option3)

    return max(dp)  # Maximum sum possible

# Example usage:
no_adjacent = [1, 2, 3, 4]
one_adjacent = [4, 4, 2, 1]
both_adjacent = [0, 1, 1, 0]

print(getMaximumSum(no_adjacent, one_adjacent, both_adjacent))  # Expected output: 13
