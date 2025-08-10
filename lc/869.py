class Solution:
    def get_powers_of_two(self):
        return [2**x for x in range(40)]

    def reorderedPowerOf2(self, n: int) -> bool:
        powers_of_two = self.get_powers_of_two()
        powers_of_two = ["".join(sorted(str(x))) for x in powers_of_two]
        return "".join(sorted(str(n))) in powers_of_two


sol = Solution()
print(sol.reorderedPowerOf2(1))
print(sol.reorderedPowerOf2(2))
print(sol.reorderedPowerOf2(5))
print(sol.reorderedPowerOf2(10))
print(sol.reorderedPowerOf2(64))
print(sol.reorderedPowerOf2(416422))
