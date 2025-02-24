class Solution:
    def __init__(self):
        self.bob_path = {}
        self.visited = []
        self.tree = []
        self.max_income = float("-inf")

    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        self.tree = [[] for _ in range(n)]
        self.bob_path = {}
        self.visited = [False] * n

        # Form tree with edges
        for edge in edges:
            self.tree[edge[0]].append(edge[1])
            self.tree[edge[1]].append(edge[0])

        # Find the path taken by Bob to reach node 0 and the times it takes to get there
        self.find_bob_path(bob, 0)

        # Find Alice's optimal path
        self.visited = [False] * n
        self.find_alice_path(0, 0, 0, amount)

        return self.max_income

    # Depth First Search to find Bob's path
    def find_bob_path(self, source_node, time):
        # Mark and set time node is reached
        self.bob_path[source_node] = time
        self.visited[source_node] = True

        # Destination for Bob is found
        if source_node == 0:
            return True

        # Traverse through unvisited nodes
        for adjacent_node in self.tree[source_node]:
            if not self.visited[adjacent_node] and self.find_bob_path(adjacent_node, time + 1):
                return True

        # If node 0 isn't reached, remove current node from path
        self.bob_path.pop(source_node, None)
        return False

    # Depth First Search to find Alice's optimal path
    def find_alice_path(self, source_node, time, income, amount):
        # Mark node as explored
        self.visited[source_node] = True

        # Alice reaches the node first
        if source_node not in self.bob_path or time < self.bob_path[source_node]:
            income += amount[source_node]
        # Alice and Bob reach the node at the same time
        elif time == self.bob_path[source_node]:
            income += amount[source_node] // 2

        # Update max value if current node is a new leaf
        if len(self.tree[source_node]) == 1 and source_node != 0:
            self.max_income = max(self.max_income, income)

        # Traverse through unvisited nodes
        for adjacent_node in self.tree[source_node]:
            if not self.visited[adjacent_node]:
                self.find_alice_path(adjacent_node, time + 1, income, amount)


s = Solution()
edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
amount = [-2, 4, 2, -4, 6]  # weight to each edge
bob = 3
# alice starts at 0
print(s.mostProfitablePath(edges=edges, bob=bob, amount=amount))


"""
Understand the constraints first - 
1. Alice starts from 0 and we want to maximize his path
2. Bob just wants to reach 0, doesn't care abt the process, we do DFS to just reach the 0th node and we have to store the path for bob. The way we do is that we add 
the current node for DFS assuming it reaches the path and call dfs() on nbrs, if any returns True for 0th node then we keep that value in our array else we pop().
Since in each iteration we add single value and pop() if no solution is lead to, we have final array of bob containing each step it took to reach 0

The reason we do not store array for bob path as we wish to do O(1) check for alice on any element that if any time before alice, has bob gone through it or not

Once we find the bob path, then for alice we go BFS as we have to maximize the value of income for alice. For this, we go in all dirs (with vis check) and 
for non visited we check if for that node, bob has crossed it at that time or before then add income accordingly.

For each bfs path of alice, we pass the income as well and we check leaf node condition that len(graph) == 1 then leaf node has come and then we do 
max_val = max(max_val, income) and return ans accordingly. 
"""
