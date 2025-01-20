s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# s = "AAAAAAAAAAAAA"

def getSameDNASequence(s:str)->list[str]:
    if len(s)<=10:
        return []
    
    n = len(s)
    # if n=10, range(1) runs once
    mapper = dict()
    for i in range(n-9):
        substr = s[i:i+10]
        if substr in mapper:
            mapper[substr]+=1
        else:
            mapper[substr]=1
    
    res = []
    for key,val in mapper.items():
        if val>1:
            res.append(key)
    
    return res

print(getSameDNASequence(s))