# https://takeuforward.org/data-structure/n-meetings-in-one-room/

n = 6
start_arr = [1,3,0,5,8,5]
end_arr = [2,4,5,7,9,9]

paired_arr = []

for x,y in zip(start_arr, end_arr):
    paired_arr.append((x,y))

paired_arr.sort(key=lambda x: x[1])

# print(paired_arr)
res_arr = []

# since the count of meetings only matter and they don't have any weight attached, the earliest meeting closing is the one to be preferred and not the earliest starting

start = paired_arr[0][1]
end = paired_arr[0][0]

res_arr = [paired_arr[0]]
counter=0

for i in range(1,len(paired_arr)):
    if paired_arr[i][0] > start:
        # mark start as new meeting and counter+=1
        start = paired_arr[i][1]
        counter+=1
        res_arr.append(paired_arr[i])

print(res_arr)
print(counter)
    