'''
Here the initial approach was to store indices of each character in mapper and then for string t, check each character if it occurs, storing it in a list.
Then we check for each index, whether indices[i] > indices[i+1]. Now this method is wrong as consider s = "acbrc" and t = "bcm". Now the correct solution is to append "m" after s to form "acbrcm" which has "bcm" in it but or solution considered indices array as [2,1] (for 'b' and 'c') and since it cares about the first occurence of character, rather than finding occurence of character after index of 'b', this approach fails.

The correct method is to get 2 pointers at start of s and t and go forward till s[i]!=t[j], when they are same then i+=1, j+=1
At the end, return len(t)-(j+1) as result
'''

def solution(s:str, t:str):
    i=0
    j=0
    
    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            i+=1
            j+=1
        else:
            i+=1 # next character
    
    return len(t)-j

print(solution(s="ajkhe", t="juh"))