nums = [1,2,3,4]

res_itr = map(lambda x: x+x, nums) # for all the numbers, takes the func lambda and does x+x
print(type(res_itr))
# print(res) # print res returns object name 

# for item in res_itr:
#     print(item)

# print(next(res_itr)) # prints 2
# print(next(res_itr)) # prints 4

# for idx, item in enumerate(res_itr):
#     print(f"i: {idx}, item: {item}")