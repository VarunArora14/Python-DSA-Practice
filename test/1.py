MOD = 10**9 + 7


class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def find_min_xor(self, num):
        node = self.root
        xor_sum = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if 1 - bit in node.children:
                xor_sum = (xor_sum << 1) | 1
                node = node.children[1 - bit]
            else:
                xor_sum = (xor_sum << 1) | 0
                node = node.children[bit]
        return xor_sum


def dfs(node, parent, tree, values):
    subtree_values = []
    for child in tree[node]:
        if child != parent:
            subtree_values.extend(dfs(child, node, tree, values))

    subtree_values.append(values[node - 1])

    if len(subtree_values) == 1:
        return [values[node - 1]]

    trie = Trie()
    for val in subtree_values:
        trie.insert(val)

    min_xor = float("inf")
    for val in subtree_values:
        min_xor = min(min_xor, trie.find_min_xor(val))

    global total_sum
    total_sum = (total_sum + min_xor) % MOD

    return subtree_values


def solve(n, edges, values):
    global total_sum
    total_sum = 0

    # Build the tree
    tree = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Perform DFS
    dfs(1, -1, tree, values)

    return total_sum


# Input
n = int(input())
edges_count = int(input())
edges_columns = int(input())
values = [int(input()) for _ in range(n)]
edges = [tuple(map(int, input().split())) for _ in range(edges_count)]

# Output
print(solve(n, edges, values))
