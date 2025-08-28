import heapq
from typing import List


def create_undirected_graph(V: int, adj: List[List[int]]):
    graph = {}
    for [src, nbr, d] in adj:
        if src not in graph:
            graph[src] = []
        if nbr not in graph:
            graph[nbr] = []

        graph[src].append((nbr, d))
        graph[nbr].append((src, d))

    return graph


def dijkstra(source: int, graph: List[List[int]]):
    q = []
    heapq.heappush(q, (0, source))
    res = [float("inf") for _ in range(len(graph) + 1)]
    res[source] = 0
    parent = [i for i in range(len(graph) + 1)]

    while len(q):
        curr_dist, top_ele = heapq.heappop(q)
        for nbr, d in graph[top_ele]:
            if curr_dist + d < res[nbr]:
                res[nbr] = curr_dist + d
                parent[nbr] = top_ele  # additional line
                heapq.heappush(q, (curr_dist + d, nbr))  # check if it's neighbours might have smaller distances

    if res[len(graph)] == float("inf"):
        return [-1]

    path = []
    n = len(graph)
    while parent[n] != n:
        path.append(n)
        n = parent[n]
    path.append(n)
    return path[::-1]


edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
graph = create_undirected_graph(len(edges), edges)
print(dijkstra(1, graph))
