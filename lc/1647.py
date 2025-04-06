class Solution:
    def minDeletions(self, s: str) -> int:
        # create map and occurences of each
        mapper = {}
        for char in s:
            if char not in mapper:
                mapper[char] = 0
            mapper[char] += 1

        value_set = set()
        duplicate_data = []
        for key, value in mapper.items():
            if value not in value_set:
                value_set.add(value)
            else:
                duplicate_data.append((key, value))

        duplicate_data.sort(key=lambda x: (-x[1]))
        print(duplicate_data)
        operation_count = 0

        for k, v in duplicate_data:
            tmp = v
            while tmp != 0 and tmp in value_set:
                tmp -= 1

            operation_count += v - tmp  # this is number of operations
            value_set.add(tmp)  # add new counter

        return operation_count


s = Solution()
string = "bbcebab"
print(s.minDeletions(s=string))
""""
We first find the occurences of each character and store them from map.

Then, we have to find the max value of these and create a set containing all numbers from 1 to max(vals) and then pop
these numbers

a->1
b->2
c->4
d->4

then set has {1,2,3,4} first and then {3} left as others are already taken. This is to check whether for duplicate value items like d->4, we can provide it a smaller value.
Since we want to minimize the operations, which check for values smaller than 4 if they exist in this set or not.

We should store those values in this set which are already allocated as this set can have 26 diff values only for each character.

We should also store the duplicate characters in array to isolate them and perform operations on
"""
