class ProductOfNumbers:
    def __init__(self):
        self.pre_mul = []
        self.product = 1

    def add(self, num: int) -> None:
        if num != 0:
            self.product *= num
            self.pre_mul.append(self.product)
        else:
            self.product = 1
            self.pre_mul = []

    def getProduct(self, k: int) -> int:
        if k == len(self.pre_mul):
            return self.pre_mul[-1]
        elif k > len(self.pre_mul):
            return 0
        else:
            return int(
                self.pre_mul[-1] / self.pre_mul[-1 - k]
            )  # divided by 1 element before kth element from end to get the prod of last k elements


s = ProductOfNumbers()


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

"""
Here we use prefix array to store the product of numbers. The problem is that if we encounter the 0, we must have a startegy for this. For this, we can see that if curr number is
0 then we set the product value as 1 as default value.
We also store the elements appended to the array and use elements pre_mul[i] to store the product of numbers. For elements with 0, we store the product value as 1.
The reason we need to store the product variable is for '0' value cases
"""
