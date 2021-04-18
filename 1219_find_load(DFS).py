for test in range(10):
    T, N = map(int, input().split())
    graph = [[] * 1 for _ in range(100)]
    putnum = list(map(int, input().split()))
    for i in range(0,len(putnum),2):
        graph[putnum[i]].append(putnum[i+1])
    visited = [False] * 100
    res = []

    def dfs(graph, v, visited):
        visited[v] = True
        if visited[99] == True:
            res.append(1)
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)
    dfs(graph,0,visited)
    if len(res) > 0:
        print("#{} {}".format(T, 1))
    else:
        print("#{} {}".format(T, 0))