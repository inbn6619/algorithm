from collections import deque

N, M = map(int, input().split()) # N == num, M == 관계 수

grahp = [[] for _ in range(N + 1)]

for m in range(M):
    a, b = map(int, input().split()) # 친구
    grahp[a].append(b)
    grahp[b].append(a)


def bfs(V):
    arr = [0] * (N + 1)
    queue = deque([V])
    visited = list()

    while queue:
        node = queue.popleft()

        for i in grahp[node]:

            if i not in visited:
                arr[i] = arr[node] + 1
                visited.append(i)
                queue.append(i)
                
    return sum(arr)

result = list()

for n in range(1, N + 1):
    result.append(bfs(n))

print(result.index(min(result)) + 1)
