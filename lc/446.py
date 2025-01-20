class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return 0 # not possible
        mem = [defaultdict(int) for _ in range(n)] # dp
        res = 0
        
        for i in range(n):
            x = nums[i]  # curr number
            for j in range(i):
                y = nums[j] # number before current index
                diff = x - y # difference between current and previous number
                
                subs = mem[j][diff] # number of subsequences previously which had the same difference, i.e. how many times current number can form an arithmetic progression with the number at index j
                res += subs # add to the result
                mem[i][diff] += subs + 1 # update the number of times a given difference was found so the numbers at the next index can use the data to form subsequences
        
        return res