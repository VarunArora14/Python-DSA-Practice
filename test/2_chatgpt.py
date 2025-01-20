def process_queries(n, array, queries):
    results_sum = 0

    for query in queries:
        t, b, c = query
        if t == 1:
            # Update the array
            array[b - 1] = c
        elif t == 2:
            # Count subarrays containing A[b-1] with max - min <= c
            b_idx = b - 1
            total_count = 0

            for start in range(n):
                min_val = float("inf")
                max_val = float("-inf")
                contains_b = False

                for end in range(start, n):
                    min_val = min(min_val, array[end])
                    max_val = max(max_val, array[end])
                    if end == b_idx:
                        contains_b = True

                    if contains_b and max_val - min_val <= c:
                        total_count += 1
                    elif max_val - min_val > c:
                        break

            results_sum += total_count

    return results_sum


# Input these as n = int(input()),
"""
arr = []
queries = []

for _ in range(n):
    arr.append(int(input()))

for _ in range(q):
    queries.append(int(input()))
"""

# Sample Test case
n = 3
array = [1, 2, 8]
queries = [(2, 2, 5)]  # Single query as described in the problem

# case 2
n = 3
array = [2, 1, 1]
queries = [
    (1, 2, 3),  # Update: A[2] = 3
    (2, 2, 1),  # Count subarrays containing A[2] with max-min <= 1
]

# Process and Output Result
result = process_queries(n, array, queries)
print(result)
