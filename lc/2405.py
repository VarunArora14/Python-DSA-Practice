
s = "ssssss"
start=0
pos=start
end=  len(s)

store = set()

substrCount=1
while pos<end:
    print(pos)
    if s[pos] in store:
        substrCount+=1
        print(f"substr -> start: {start}, end: {pos-1}")
        start=pos
        store.clear()
    else:    
        store.add(s[pos])
        pos+=1

print(substrCount)