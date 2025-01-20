def bitOperation(a: int, b: int):
    return a & b


def findOneBits(a: int) -> int:
    count = 0
    while a > 0:
        if a & 1:
            count += 1
        a = a >> 1  # right shift 1 bit

    return count


def findClosestTwoPower(number=1e4) -> int:
    p = 1
    while pow(2, p) < number:
        p += 1
    return p - 1


print(bin(10000))
# zip
print(findClosestTwoPower())

print(bitOperation(1, 3))

print(findOneBits(1))
print(findOneBits(2))
print(findOneBits(3))
print(findOneBits(7))
