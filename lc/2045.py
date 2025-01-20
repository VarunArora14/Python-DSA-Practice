
# print(sorted(arr, key=lambda x: x[1]))

# arr = [[1,3,2],[4,5,2],[1,5,5]]
arr = [[1,3,2],[4,5,2],[2,4,3]]
# arr = [[1,5,3],[1,5,1],[6,6,5]]

arr = sorted(arr, key= lambda x: (x[1],x[0]))



# We cannot store max value for each time till max value of endTime as it ranges to 1e9
# we rather store the state of max value for each index of element where we say that for current element ending, 
# the max element is this idx_max_vals[i]

curr_max_ele =0
for a in arr:
    curr_max_ele = max(curr_max_ele, a[2])

print("current max val", curr_max_ele)

idx_max_vals = [0 for _ in range(len(arr))]
idx_max_vals[0]=arr[0][2]

for i in range(1, len(arr)):
    idx_max_vals[i] = max(idx_max_vals[i-1], arr[i][2]) # store the max value for each index till now

print("idx_max_vals", idx_max_vals)

for i in range(1, len(arr)):
    if arr[i-1][1] <= arr[i][0]:
        curr_max_ele = max(curr_max_ele, arr[i-1[2] + arr[i]][2])
        
        print("hey",i, idx_max_vals[i-1] + arr[i][2])

print(curr_max_ele)