def solution(n, computers):
    answer = 0
    visited = [[] for _ in range(200)]
    tmp = [[] for _ in range(n)]

    for j in range(n):
        for i in range(n):
            if i == j:
                continue
            if computers[j][i] == 1:
                tmp[i].append(j)

    def dfs(start, t):
        while start:
            node = start.pop()
            if t in tmp[node]:
                visited[t] = 1
                visited[node] = 1
            dfs(tmp[node], node)
        return

    for t in range(len(tmp)):
        if not visited[t]:
            dfs(tmp[t], t)
            answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1
print(solution(3, [[1, 0, 1], [0, 1, 1], [0, 0, 1]])) # 3