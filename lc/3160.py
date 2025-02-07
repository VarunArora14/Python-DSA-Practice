from typing import List, Set, Dict
from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        number_color_mapper = dict()
        color_number_mapper = defaultdict(set)
        query_results = []

        for [x, y] in queries:
            if y not in color_number_mapper:
                color_number_mapper[y] = set()

            if x not in number_color_mapper:
                # element occurs first time
                number_color_mapper[x] = y
                color_number_mapper[y].add(x)
            else:
                # number exists with some color but mapping to color might change
                if number_color_mapper[x] != y:
                    # not the existing color
                    existing_color = number_color_mapper[x]
                    number_color_mapper[x] = y
                    color_number_mapper[existing_color].remove(x)
                    if color_number_mapper[existing_color] == set():
                        del color_number_mapper[existing_color]
                    color_number_mapper[y].add(x)
            query_results.append(len(color_number_mapper.keys()))
        return query_results


limit = 4
queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
s = Solution()
print(s.queryResults(queries=queries, limit=limit))


"""
Things to consider - 
- same ball can come again and be coloured to any other same color
- 2 balls can have same color and same ball can have later another color
- check for each query

The above code is not optimised as it depends on len of map keys() to get the answer which in itself takes O(n) operation
"""
