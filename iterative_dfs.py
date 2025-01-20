def addEdge(graph:dict, u:int, v:int):
    if u not in graph:
        graph[u]=[]
    if v not in graph:
        graph[v]=[]
    
    # for bi-drecitonal graph
    # if v not in graph:
    #     graph[v]=[]
    
    graph[u].append(v)
    # graph[v].append(u)


def dfsIterative(graph:dict, source:int):
    
    # we use stack for iterative where we can append the neighbours to end of stack and use the last element as the top
    # for DFS
    st = []
    vis = set()
    
    st.append(source)
    
    while len(st):
        top = st.pop()
        
        if top not in vis:
            vis.add(top)
            print(top, end=' ')
        
        for nbr in graph[top]:
            st.append(nbr) # add to end and pick later the last element which is then the top element of stack for dfs
    
g={}
addEdge(g,1,2)
addEdge(g,2,5)
addEdge(g,5,6)
addEdge(g,2,3)
addEdge(g,3,4)
addEdge(g,4,6)
dfsIterative(graph=g, source=1)