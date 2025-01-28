from typing import List
from collections import defaultdict, deque


class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])
            indegree[edge[1]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        nodePrerequisites = defaultdict(set)

        while q:
            node = q.popleft()

            for adj in adjList[node]:
                # Add node and prerequisite of the node to the prerequisites of adj
                nodePrerequisites[adj].add(node)
                for prereq in nodePrerequisites[node]:
                    nodePrerequisites[adj].add(prereq)

                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)

        answer = []
        for q in queries:
            answer.append(q[0] in nodePrerequisites[q[1]])

        return answer


num_courses = 2
prerequisites = [[1, 0]]
queries = [[0, 1], [1, 0]]
s = Solution()
print(s.checkIfPrerequisite(prerequisites=prerequisites, queries=queries, numCourses=num_courses))

"""
Here for each of the queries, we have to see that whether an element happens to be parent of a node as per the directed graph. This problem seems to be similar to DSU
where we store the nodes and their parents to further perform operations. Since in this, any node in the parent/grandparents can be seen as part of the queries,
rather than normalising paths which are long, we let them be as any of the middle element can be part of the query. Ex: 1->2->3->5->7->8->9, the query can be to see if 1 is
parent of 9 or 5 is parent of 9 etc. So we cannot have just 1->9 as the value to be stored or traversed
"""
