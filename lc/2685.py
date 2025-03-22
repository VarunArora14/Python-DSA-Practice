from typing import Dict, List, Set


class Solution:
    def check_connected_component(self, node: int, graph: Dict[int, List[int]], vis: Set):
        q = []
        q.append(node)
        vis.add(node)
        flag = True  # go through the component and mark it
        edges_count = len(graph[node])
        component_size = 1
        while len(q):
            last = q.pop()
            print(edges_count, last, len(graph[last]))
            if edges_count != len(graph[last]):
                flag = False
            for nbr in graph[last]:
                if nbr not in vis:
                    vis.add(nbr)
                    component_size += 1
                    q.append(nbr)

        if component_size != edges_count + 1:
            return False
        return flag

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph: Dict[int, List[int]] = dict()
        unseen_nodes = set()
        vis = set()
        res = 0

        for [u, v] in edges:
            if u not in graph:
                graph[u] = []

            if v not in graph:
                graph[v] = []

            graph[u].append(v)
            graph[v].append(u)

            unseen_nodes.add(u)
            unseen_nodes.add(v)

        for k in unseen_nodes:
            if k not in vis:
                if self.check_connected_component(graph=graph, node=k, vis=vis):
                    print("hey")
                    res += 1

        # if other nodes not as edges, then they are single components
        res += n - len(vis)
        return res


s = Solution()
n = 4
edges = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(s.countCompleteComponents(edges=edges, n=n))

"""
The core idea was to count the number of connected components in the graph with additional situations - 

- The components must have all the edges connecting to each other node in the component. This means graph[nbr] length must be component size - 1. If this fails, 
return False as this is not a valid component
- There can be nodes with no edges but solo nodes, consider them also as components as part of the answer
"""
