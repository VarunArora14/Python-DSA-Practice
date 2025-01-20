def compareSets():
    s1 = set([1,3,5,9])
    s2 = set([5,3,9,1])
    print(f"sets equality: {s1==s2}")


def compareSortedLists():
    l1 = [1,2,3,4]
    l2 = [1,2,4,3]

    print(f"Sorted compare: {sorted(l1) == sorted(l2)}")
compareSortedLists()