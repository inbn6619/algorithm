import sys

read = sys.stdin

N, M = map(int, read.readline().split()) # 정점, 간선

matrix = [[] for i in range(N + 1)]

for m in range(M):
    a, b = map(int, read.readline().split())
    matrix[a].append(b)
    matrix[b].append(a)

visited = list()

cnt = 0

def dfs(graph, V):
    stack = list()
    stack.append(V)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])


for i in range(1, len(matrix)):
    if i not in visited:
        cnt += 1
        dfs(matrix, i)


print(cnt)