def addEdge(graph:dict, u:int, v:int):
    if u not in graph:
        graph[u]=[]
    if v not in graph:
        graph[v]=[]
    
    graph[u].append(v)
    
    # for bi-drecitonal graph
    # graph[v].append(u)

def bfs(graph:dict, source:int, vis:set):
    print()
    q = []
    
    q.append(source)
    
    while len(q):
        top = q[0]
        # print("top: ", top)
        q=q[1:]
        
        if top not in vis:
            vis.add(top)
            print(top, end=' ')
            
        for nbr in graph[top]:
            if nbr not in vis:
                q.append(nbr)


def bfsDisconnected(graph:dict):
    
    keys = list(graph.keys())
    print(keys)
    
    vis = set()
    for key in keys:
        if key not in vis:
            bfs(graph=graph, source=key, vis=vis)
        
g={}
addEdge(g,1,2)
addEdge(g,2,5)
addEdge(g,5,6)
addEdge(g,2,3)
addEdge(g,3,4)
addEdge(g,4,6)
addEdge(g,7,8)
bfsDisconnected(graph=g)        
    