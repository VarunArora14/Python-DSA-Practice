def build_graph(edges, n):
    """Build adjacency list representation of the tree."""
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def dfs(node, parent, graph, values, subtree_vals):
    """DFS to collect values in subtree."""
    subtree_vals[node].add(values[node - 1])

    for child in graph[node]:
        if child != parent:
            dfs(child, node, graph, values, subtree_vals)
            subtree_vals[node].update(subtree_vals[child])


def get_min_xor(values):
    """Calculate minimum XOR value for a set of numbers."""
    if len(values) == 1:
        return list(values)[0]

    values = list(values)
    min_xor = float("inf")
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            min_xor = min(min_xor, values[i] ^ values[j])
    return min_xor


def solve_tree_min_xor(n, m, two, values, edges):
    """Solve the tree minimum XOR sum problem."""
    MOD = 10**9 + 7

    # Build tree
    graph = build_graph(edges, n)

    # Store values in subtrees
    subtree_vals = [set() for _ in range(n + 1)]

    # Get subtree values starting from root
    dfs(1, 0, graph, values, subtree_vals)

    # Calculate answer for each node
    total_sum = 0
    for node in range(1, n + 1):
        if len(subtree_vals[node]) == 1:
            # If subtree has only one node, use its value
            result = list(subtree_vals[node])[0]
        else:
            # Otherwise find minimum XOR
            result = get_min_xor(subtree_vals[node])
        total_sum = (total_sum + result) % MOD

    return total_sum


def main():
    # Read input
    n = int(input())  # number of elements in a
    m = int(input())  # number of rows in edges
    two = int(input())  # number of columns in edges (always 2)

    # Read values array
    values = []
    for _ in range(n):
        values.append(int(input()))

    # Read edges
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append([u, v])

    # Solve and print result
    result = solve_tree_min_xor(n, m, two, values, edges)
    print(result)


if __name__ == "__main__":
    main()
