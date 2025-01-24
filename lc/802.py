from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0] * n
        safe_states = []

        def dfs(state: int) -> bool:
            if visited[state] == 1:
                return False
            if visited[state] == 2:
                return True

            visited[state] = 1
            for neighbor in graph[state]:
                if not dfs(neighbor):
                    return False

            visited[state] = 2
            return True

        for state in range(n):
            if visited[state] == 2:
                safe_states.append(state)
            elif visited[state] == 0 and dfs(state):
                safe_states.append(state)

        return safe_states


graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
s = Solution()
print(s.eventualSafeNodes(graph=graph))
# we know that this list is sorted so we can think if this information is useful to us


"""
Currently, we have for each index i, array of elements representing the edges to them diectly from i->graph[i] as directed edges. Now, we have to first determine the terminal nodes and then find those SAFE NODES(which end up going towards terminal nodes).
Note - Terminal nodes are themselves safe nodes.

Important thing to notice - since in a path from a node1 to a terminal node we have x number of nodes, it means all those nodes will also have path to terminal node.

We need DFS for this to have condition that if node has no edges then we have reached a terminal node and so mark the path nodes in ans array and add them in visited set.

We need to maintain set of nodes which are in path (for O(1) search) and set of safe nodes(that have a path to terminal node and find them in O(1) time)
"""
