# 1번 노드는 start
def solution(n, edge):
    from collections import deque
    nodes = [[] for _ in range(n + 1)]
    num = int(1e9)
    dis = [num] * (n+1)

    for a, b in edge:
        # print(a, b)
        nodes[a] += [b]
        nodes[b] += [a]

    def bfs(start, grahp):
        queue = deque([start])
        dis[start] = 0

        while queue:
            node = queue.popleft()

            for i in grahp[node]:
                if dis[i] == num:
                    dis[i] = dis[node] + 1
                    queue.append(i)
        

            
    bfs(1, nodes)

    answer = dis[1:].count(max(dis[1:]))
    return answer

print(solution(8, 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2], [6, 7], [5, 8]]))