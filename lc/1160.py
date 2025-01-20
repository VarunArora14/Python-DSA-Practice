def countCharacters(self, words: list[str], chars: str) -> int:
    '''
    Traverse through each word in words, then through each character and check if characters occurs
    in both chars and word, count of char in word <= count of char in chars
    '''
    mapper = dict()
    res=0
    
    for c in chars:
        if c in mapper:
            mapper[c]+=1
        else:
            mapper[c]=1
    
    for w in words:
        m = dict()
        for char in w:
            if char in m:
                m[char]+=1
            else:
                m[char]=1
        flag=True
        for key, val in m.items():
            if key not in m or val > mapper[key]:
                flag=False
        
        if flag==True:
            res+=len(w)
    
    return res

# we can compare word.count(char) to match chars

# def countCharacters(self, words: List[str], chars: str) -> int:  
#     ans = 0
#     for word in words:
#         for ch in word:
#             if word.count(ch) > chars.count(ch):
#                 break
#         else:
#             ans += len(word)   
#     return ans