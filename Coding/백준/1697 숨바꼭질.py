from collections import deque

N, K = map(int, input().split()) # 현재, 동생 위치

nums = 100001

matrix = [0] * nums

def bfs(V):
    queue = deque()
    queue.append(V)

    while queue:
        node = queue.popleft()

        if node == K:
            print(matrix[node])
            break
        for n in (node - 1, node + 1, node * 2):
            if 0 <= n < nums and not matrix[n]:
                matrix[n] = matrix[node] + 1
                queue.append(n)

bfs(N)
