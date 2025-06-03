class DSU:
    def __init__(self, n:int):
        self.parentMapper = self.__create(n=n)
        
    def __create(self, n:int):
        parentMapper = {i: i for i in range(1,n+1)}
        return parentMapper
        

    def findParent(self, node:int):
        if self.parentMapper[node]==node:
            return node
        else:
            # path compression
            self.parentMapper[node] = self.findParent(self.parentMapper[node])
            return self.parentMapper[node]


    def join(self, u:int, v:int):
        parent_of_u = self.findParent(u)
        parent_of_v = self.findParent(v)
        
        # same component
        if parent_of_u==parent_of_v:
            return
        
        else:
            # make them part of same component
            self.parentMapper[parent_of_v] = parent_of_u
            
d=DSU(10)
d.join(1,4)
d.join(4,7)
d.join(8,9)
print(d.parentMapper)