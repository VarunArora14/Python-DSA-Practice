lines = input().split("\n")
farr = []
sarr = []
for l in lines:
    print(l)
    f,s = l.split('   ')
    farr.append(int(f))
    sarr.append(int(s))
print(farr,sarr)