def dfs(g, i, visited):
    visited[i] = 1
    print(arr[i], end =' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

graph = [
    [0,1,1,0,0,0],
    [1,0,0,1,0,0],
    [1,0,0,1,0,0],
    [0,1,1,0,1,1],
    [0,0,0,1,0,1],
    [0,0,0,1,1,0]
]
arr = ['문별','솔라','휘인','쯔위','선미','화사']

visited = [0]*len(graph)
dfs(graph, 0, visited)