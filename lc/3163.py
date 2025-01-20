def compressedString(word:str):
    n = len(word)
    res=""
    
    i=0
    
    while i<n:
        curr_char = word[i]
        length=0
        while i+length<n and word[i+length] == curr_char and length<9:
            length+=1
        res+=str(length) + curr_char
        i+=length # go to i+length pos as it has be considered
    
    return res

print(compressedString("abcde"))