class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        ops = 0
        arr = [s]
        if start <= int(s) <= finish:
            print(int(s))
            ops += 1
        tmp = []
        while len(arr):
            tmp = []  # initialise them empty
            for i, a in enumerate(arr):
                for i in range(1, limit + 1):
                    string = str(i) + a
                    if start <= int(string) <= finish:
                        # print(string)
                        ops += 1
                        tmp.append(string)

            arr = tmp
            print("tmp", tmp)

        return ops


sol = Solution()

start = 20
finish = 1159
limit = 5
s = "20"
print(sol.numberOfPowerfulInt(start, finish, limit, s))


"""
Consider we have s string, we check if len of s is less than limit and then add characters 1 to 9 as prefix each time with check if int(s) >=start and <=finish
and have to consider following base cases - 

if no s found between start and finish 
"""
