from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

class Solution:
    def twoSum(self, nums, target):
        index_map = {}
        for index, num in enumerate(nums):
            if target - num in index_map:
                return index_map[target - num], index
            index_map[num] = index

        return -1
s=Solution()
print(s.twoSum(nums=[1,2,3,9], target=8))
