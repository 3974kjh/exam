from collections import deque

N, M, v = map(int,input().split())
tree = []
A = []
graph = [[] * 1 for _ in range(N + 1)]
for i in range(M):
    A = map(int, input().split())
    tree.extend(A)
for i in range(0, len(tree),2):
    graph[tree[i]].append(tree[i+1])
    graph[tree[i+1]].append(tree[i])
for i in range(N+1):
    if len(graph[i]) > 1:
        graph[i].sort()

visited = [False] * (N+1)
def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
dfs(graph, v, visited)
print('')
visited = [False] * (N+1)
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
bfs(graph, v, visited)