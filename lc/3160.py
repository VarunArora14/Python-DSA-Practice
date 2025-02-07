from typing import List, Set, Dict
from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_number_to_color_mapping = dict()
        color_to_number_mapping = defaultdict(set)
        query_results = []
        distinct_colors = 0

        for ball_number, new_color in queries:
            if ball_number in ball_number_to_color_mapping:
                old_color = ball_number_to_color_mapping[ball_number]
                color_to_number_mapping[old_color] -= 1
                if color_to_number_mapping[old_color] == 0:
                    del color_to_number_mapping[old_color]  # imp
                    distinct_colors -= 1

            ball_number_to_color_mapping[ball_number] = new_color
            if new_color in color_to_number_mapping:
                color_to_number_mapping[new_color]
            else:
                distinct_colors += 1
                color_to_number_mapping[new_color] = 1

            query_results.append(distinct_colors)
        return query_results


limit = 4
queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
# queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
s = Solution()
print(s.queryResults(queries=queries, limit=limit))


"""
Things to consider - 
- same ball can come again and be coloured to any other same color
- 2 balls can have same color and same ball can have later another color
- check for each query

The above code is not optimised as it depends on len of map keys() to get the answer which in itself takes O(n) operation
"""
