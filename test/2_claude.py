def count_valid_subarrays(arr, target, diff_limit, bi_number):
    """Count subarrays containing target with max-min difference <= diff_limit"""
    count = 0
    n = len(arr)
    arr.sort()
    s = set()

    # For each possible start point
    for i in range(n):
        min_val = float("inf")
        max_val = float("-inf")
        found_target = False

        # For each possible end point
        for j in range(i, n):
            min_val = min(min_val, arr[j])
            max_val = max(max_val, arr[j])

            # print(arr[i : j + 1])
            if bi_number in arr[i : j + 1]:
                found_target = True

            # If target number is found and difference condition is met
            if found_target and (max_val - min_val) <= diff_limit:
                if str(arr[i : j + 1]) not in s:
                    print(arr[i : j + 1])
                    s.add(str(arr[i : j + 1]))
                    count += 1
            # If difference exceeds limit, no need to check further
            elif max_val - min_val > diff_limit:
                break
    print(count)
    return count


def solve():
    # Read input
    N = int(input())  # Number of elements in array A
    Q = int(input())  # Number of queries

    # Read array A
    A = []
    for _ in range(N):
        A.append(int(input()))

    # Read and process queries
    total_sum = 0
    T = []
    B = []
    C = []

    # Read all query parameters
    for _ in range(Q):
        T.append(int(input()))
    for _ in range(Q):
        B.append(int(input()))
    for _ in range(Q):
        C.append(int(input()))

    total_sum = 0
    # Process each query
    for i in range(Q):
        if T[i] == 1:
            # Update query: change A[B[i]-1] to C[i]
            A[B[i] - 1] = C[i]
        else:  # T[i] == 2
            # Count query
            result = count_valid_subarrays(
                A, B[i], C[i], A[B[i] - 1]
            )  # Bith number should be in the subarray
            total_sum += result

    # Print result

    print(total_sum)
    return total_sum


# Run the solution
solve()
