from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<=0:
            return []

        if numRows ==1:
            return [[1]]
        
        if numRows == 2:
            return [
                [1], 
                [1,1]
            ]
        arr = [
            [1],
            [1,1]
        ]
        
        if numRows == 1 or numRows==2:
            return arr[numRows-1]

        for i in range(2, numRows):
            newRow = [1]
            for j in range(1, i):
                newRow.append(arr[i-1][j] + arr[i-1][j-1])
            newRow.append(1)
            arr.append(newRow)
        
        return arr

sol = Solution()
print(sol.generate(7))

"""
Pascal's Triangle - Base cases we know are the first and 2nd rows - make a check for it

- For next rows, visualise the array and consider the first and last elements to be always 1
- Find the pattern that prev row columns sum makes the current row value as arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
- Create the final array and then run tests before submit

"""