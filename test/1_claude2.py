def build_tree(n, edges):
    """Create adjacency list representation of tree."""
    tree = [[] for _ in range(n + 1)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    return tree


def get_subtree_values(node, parent, tree, values, subtree_vals):
    """Collect all values in the subtree of each node using DFS."""
    # Initialize with current node's value
    curr_subtree = {values[node - 1]}

    # Collect values from all child subtrees
    for child in tree[node]:
        if child != parent:
            child_values = get_subtree_values(child, node, tree, values, subtree_vals)
            curr_subtree.update(child_values)

    # Store the subtree values for current node
    subtree_vals[node] = curr_subtree
    return curr_subtree


def get_min_xor(values):
    """Find minimum XOR value between any two numbers in the set."""
    if len(values) == 1:
        return list(values)[0]  # For leaf nodes

    min_xor = float("inf")
    values = list(values)

    # Compare each pair of values
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            min_xor = min(min_xor, values[i] ^ values[j])

    return min_xor


def solve(n, edges, values):
    """Main solution function."""
    MOD = 10**9 + 7

    # Build tree
    tree = build_tree(n, edges)

    # Dictionary to store subtree values for each node
    subtree_vals = {}

    # Get all subtree values starting from root (node 1)
    get_subtree_values(1, 0, tree, values, subtree_vals)

    # Calculate answer for each node
    total = 0
    for node in range(1, n + 1):
        min_xor_val = get_min_xor(subtree_vals[node])
        total = (total + min_xor_val) % MOD

    return total


def main():
    # Read input
    n = int(input())
    m = int(input())
    two = int(input())  # Always 2 for edges

    # Read values for each node
    values = []
    for _ in range(n):
        values.append(int(input()))

    # Read edges
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append([u, v])

    # Get and print result
    result = solve(n, edges, values)
    print(result)


# Test cases
def run_test_cases():
    # Test Case 1
    print("Test Case 1:")
    n1, edges1, values1 = 2, [[1, 2]], [1, 1]
    print(solve(n1, edges1, values1))  # Expected: 1

    # Test Case 2
    print("Test Case 2:")
    n2, edges2, values2 = 3, [[1, 2], [2, 3]], [1, 2, 3]
    print(solve(n2, edges2, values2))  # Expected: 5

    # Test Case 3
    print("Test Case 3:")
    n3, edges3, values3 = 3, [[1, 2], [1, 3]], [1, 2, 3]
    print(solve(n3, edges3, values3))  # Expected: 6


if __name__ == "__main__":
    # main()
    # Uncomment to run test cases
    run_test_cases()


# def get_ans(n,m,two,a,edges):
#     result = solve(n,edges, a)
