from sortedcontainers import SortedList
from typing import Dict


class NumberContainers:
    def __init__(self):
        self.number_to_index: Dict[SortedList] = dict()
        self.index_to_number = {}

    def change(self, index: int, number: int) -> None:
        if index not in self.index_to_number:
            self.index_to_number[index] = -1
        if number not in self.number_to_index:
            self.number_to_index[number] = SortedList([])

        # remove the mapping of old number in index->old_num => remove the index from old num mapping => add to new num mapping
        if self.index_to_number[index] == -1:
            self.index_to_number[index] = number
            self.number_to_index[number].add(index)  # since no mapping of index so no replacement
        else:
            old_num = self.index_to_number[index]
            self.index_to_number[index] = number
            self.number_to_index[number].add(index)
            self.number_to_index[old_num].remove(index)  # remove from sorted list O(lgn)

    def find(self, number: int) -> int:
        if number in self.number_to_index and len(self.number_to_index[number]) > 0:
            return self.number_to_index[number][0]
        else:
            return -1


"""
We need to store the numbers in each mapping sorted as we wish to do addition and removal in max logn time!
Since we need to know which number the index already had, we store index to number mapping along with number to index sorted list mapping

We know if index does not exist, it means it can be only added to a new number's list.
Otherwise, if it has a mapping, we remove the index from old_num's list and then add it to new number's list

Then for find() we check if number exists and it's list has more than 0 elements, then we return the first element which is smallest as arr is sorted
"""


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
