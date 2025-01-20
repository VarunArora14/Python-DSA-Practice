# consider a longer string like - 'hello' , 'ahello', 'abahe' and substr='he'
# find the position of substr if it exists else return -1 with and without using existing methods

string = "hello"
string = "ahello"
# string = "abahe"
# string = "aba"

substr= 'he'

def existingMethod(string:str, substr:str):
    print(string.find(substr))

def createMethod(string:str, substr:str):
    str_i, sub_i = 0,0
    
    while str_i < len(string) and sub_i<len(substr):
        if sub_i == len(substr)-1:
            print("string found at: ", str_i - sub_i, string[str_i-sub_i: str_i+1]) # +1 as last pos is ignored
            return
        
        if string[str_i] == substr[sub_i]:
            sub_i+=1
        else:
            sub_i=0
    
        str_i+=1

    print(-1)

# existingMethod(string=string, substr=substr)
# createMethod(string, substr)

print("leetcode".find("leet"))

s = "penapple"

idx = s.find("apple")
print(s[:idx])
print(s[idx + len("apple"):])

print("code" in "code")
