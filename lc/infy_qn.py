# https://leetcode.com/discuss/interview-question/5624976/hard-infosys-qn-need-asnwers

l=1
r=11
k=1
m=1 # len of string l
n =2 # len of string r

# both l and r are smaller than 500

# print(bin(5)[2:])

for i in range(l, r+1):
    print(i, bin(i)[2:])

# 2 conditions - num%k==0 and bit of num must have 0's and count of 1s > count 0s

l = '1'
r = '110'
k=3

l = '1'
r = '111'
k=2

l='1'
r='11'
k=1

start = int(l,2)
end = int(r, 2)
print(start, end)

def countOnesMore(i):
    bin_str = bin(i)[2:]
    ones_count = bin_str.count('1')
    zeros_count = bin_str.count('0')
    
    return  ones_count>zeros_count

counter=0
for i in range(start, end+1):
    if i%k==0 and countOnesMore(i)==True:
        counter+=1
        print(bin(i)[2:])

print("counter: ", counter)

