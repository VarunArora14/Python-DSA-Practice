from collections import defaultdict
from heapq import heappop, heappush
from typing import Dict, List, Set, Tuple


class Solution:
    def dfs(
        self,
        node: int,
        vis: Set,
        res_mapper: Dict,
        graph: Dict[int, List[Tuple[int]]],
        n: int,
        curr_sum=0,
    ):
        if node == n - 1:
            if curr_sum not in res_mapper:
                res_mapper[curr_sum] = 0
            res_mapper[curr_sum] += 1
            return

        for nbr, wt in graph[node]:
            if nbr not in vis:
                vis.add(nbr)
                # print(node, nbr, wt)
                self.dfs(node=nbr, vis=vis, res_mapper=res_mapper, graph=graph, curr_sum=curr_sum + wt, n=n)
                # print(vis)
                vis.remove(nbr)

    def countPathsTLE(self, n: int, roads: List[List[int]]) -> int:
        graph: Dict[int, List[Tuple[int]]] = dict()
        for [u, v, w] in roads:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []

            graph[u].append((v, w))
            graph[v].append((u, w))

        print(graph)
        res_mapper = {}
        vis = set()
        vis.add(0)
        self.dfs(node=0, vis=vis, res_mapper=res_mapper, graph=graph, n=n)
        min_sum, max_ways = float("inf"), 0
        for key_sum, val_count in res_mapper.items():
            if min_sum == key_sum:
                max_ways = max(val_count, max_ways)
            elif min_sum > key_sum:
                min_sum = key_sum
                max_ways = val_count

        return max_ways

        # Do DFS from start and find all roads to n-1

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # create adjacency list
        adj_list = defaultdict(list)
        for i, j, k in roads:
            adj_list[i].append((j, k))
            adj_list[j].append((i, k))

        start = 0
        end = n - 1

        # set minimum distance of all nodes but start to infinity.
        # min_dist[i] = [minimum time from start, number of ways to get to node i in min time]
        min_dist = {i: [float("inf"), 0] for i in adj_list.keys()}
        min_dist[start] = [0, 1]

        # Heap nodes in the format (elapsed time to get to that node, node index)
        # This is done so as to allow the heap to pop node with lowest time first
        # Push first node to heap.
        heap = [(0, start)]
        while heap:
            elapsed_time, node = heappop(heap)
            # if nodes getting popped have a higher elapsed time than minimum time required
            # to reach end node, means we have exhausted all possibilities
            # Note: we can do this only because time elapsed cannot be negetive
            if elapsed_time > min_dist[end][0]:
                break
            for neighbor, time in adj_list[node]:
                # check most expected condition first. Reduce check time for if statement
                if (elapsed_time + time) > min_dist[neighbor][0]:
                    continue
                # if time is equal to minimum time to node, add the ways to get to node to
                # the next node in minimum time
                elif (elapsed_time + time) == min_dist[neighbor][0]:
                    min_dist[neighbor][1] += min_dist[node][1]
                else:  # node has not been visited before. Set minimum time
                    min_dist[neighbor][0] = elapsed_time + time
                    min_dist[neighbor][1] = min_dist[node][1]
                    heappush(heap, (elapsed_time + time, neighbor))

        return min_dist[end][1] % (pow(10, 9) + 7)


s = Solution()
n = 7
roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
print(s.countPaths(n=n, roads=roads))
