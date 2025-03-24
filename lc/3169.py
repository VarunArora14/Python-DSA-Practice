from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        startx, endx = -1, -1
        if len(meetings) == 1:
            return days - (meetings[0][1] - meetings[0][0] + 1)

        meetings.sort(key=lambda x: (x[0], x[1]))
        # print("meetings", meetings)
        startx = meetings[0][0]
        endx = meetings[0][1]
        res = 0
        for i in range(1, len(meetings)):
            if endx >= meetings[i][0]:
                endx = max(endx, meetings[i][1])  # important to keep the largest value
            else:
                # print(endx, startx)
                res += endx - startx + 1
                startx = meetings[i][0]
                endx = meetings[i][1]

        # print("hi", endx, startx)
        res += endx - startx + 1

        # print(res)
        return days - res


s = Solution()
days = eval(input())

meetings = eval(input())
print(s.countDays(days=days, meetings=meetings))
