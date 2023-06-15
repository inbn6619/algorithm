from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in range(1, 1+N):
        if not visited[i] and matrix[v][i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        node = queue.popleft()

        print(node, end=' ')

        for i in range(1, N + 1):
            if not visited[i] and matrix[node][i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())

matrix = [[False]*(N+1) for i in range(N+1)]


for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b]=matrix[b][a]=True

# print(matrix)


# for k in matrix:
#     k.sort()

visited = [False] * (N + 1)
visited_B = [False] * (N + 1)

dfs(matrix, V, visited)
print()
bfs(matrix, V, visited_B)
