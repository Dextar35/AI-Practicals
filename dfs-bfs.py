def dfs(graph,visited,node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph,visited,neighbour)

def bfs(visited,vertex,graph):
    visited.add(vertex)
    queue = []
    queue.append(vertex)
    while queue:
        v = queue.pop(0)
        print(v)
        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
graph = {
    0 : [1,2,3],
    1 : [0],
    2 : [0,2,3,4],
    3 : [0,2],
    4 : [2]
}

visited = set()

dfs(graph,visited,0)

visited.clear()

bfs(visited,0,graph)
