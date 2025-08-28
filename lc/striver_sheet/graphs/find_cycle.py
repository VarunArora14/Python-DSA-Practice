from collections import deque


def create_graph(v: int):
    graph = {}
    for i in range(1, v + 1):
        graph[i] = []
    return graph


def add(graph: dict, src: int, dest: int):
    graph[src].append(dest)
    graph[dest].append(src)


graph = create_graph(8)
add(graph, 1, 2)
add(graph, 1, 3)
add(graph, 3, 4)
add(graph, 3, 7)
add(graph, 7, 8)
add(graph, 2, 6)
add(graph, 5, 2)

# graph = create_graph(8)
# add(graph, 1, 2)
# add(graph, 2, 3)
# add(graph, 4, 5)
# add(graph, 6, 5)
# add(graph, 4, 6)
# add(graph, 8, 7)


class Solution:
    def dfs(self, graph: dict, visited_set: set, src: int, parent: int):
        visited_set.add(src)
        for nbr in graph[src]:
            if nbr == parent:
                continue

            if nbr in visited_set:
                print(visited_set, nbr)
                print(nbr, parent)
                return True

            if self.dfs(graph, visited_set, nbr, src):
                return True

        return False

    def bfs(self, graph: dict, visited_set: set, src: int, parent: int):
        visited_set.add(src)
        q = deque()
        q.append((src, parent))
        while len(q):
            (node, node_parent) = q.popleft()
            for nbr in graph[node]:
                if nbr == node_parent:
                    continue

                if nbr in visited_set:
                    print("cycle detected at", nbr)
                    return True

                q.append((nbr, node))
                visited_set.add(nbr)

        return False

    def find_cycle(self, graph: dict):
        visited_set = set()
        # print(graph)
        for i in range(1, len(graph) + 1):
            if i not in visited_set:
                print("cycle search starts at ", i)

                # replace self.bfs with self.dfs for depth first search implementation
                if self.bfs(graph, visited_set, i, -1):
                    print("Cycled detected from node: ", i)
                    return True

        return False


sol = Solution()
print(sol.find_cycle(graph))
