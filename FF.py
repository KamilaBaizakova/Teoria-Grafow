graph,V,int_max = list(),6,999999
def bfs(s,t,parent):
    global V,graph
    vis =[False for i in range(V)] 
    q = list() 
    q.insert(0,s)
    vis[s]=True
    parent[s]=-1
    while len(q)!=0:
        u = q.pop()
        for i in range(V):
            if not vis[i] and graph[u][i]>0:
                q.insert(0,i)
                parent[i]=u
                vis[i]=True
    return vis[t] 
                  
def fordFulkerson(s,t):
    global graph,V,int_max
    parent, max_flow = [0 for i in range(V)],0
    
    while bfs(s,t,parent):
        path_flow = int_max
        v = t
        while v!=s: 
            u = parent[v]
            path_flow = min(path_flow,graph[u][v])
            v = parent[v] 
        v = t
        while v!=s: 
            u = parent[v]
            graph[u][v]-= path_flow 
            graph[v][u]+= path_flow 
            v = parent[v]
        max_flow += path_flow 
    return max_flow



  
with open('graph.txt', 'r') as f:
   graph = [[int(num) for num in line.split(',')] for line in f]



src = 0; sink = 5
  
print("Max flow:",fordFulkerson(src,sink))
 

