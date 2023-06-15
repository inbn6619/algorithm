def solution(maps):
    from collections import deque

    n = len(maps)
    board = [[-1] * n for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    answer = 0
    
    def bfs(x, y):
        maps[y][x] = 0
        board[y][x] = 1
        queue = deque([[[x, y]]])
        cnt = 1

        while queue[0]:
            cnt += 1
            tmp = list()
            node = queue.popleft()
            check = False
            coor = list()

            for _ in range(len(node)):
                x, y = node.pop()
                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y

                    if 0 <= nx < n and 0 <= ny < n and maps[ny][nx] == 1:
                        tmp.append([nx, ny])
                        coor.append(abs(sum(n-1, n-1) - sum(nx, ny)))

            for j in range(len(tmp)):
                board[ny][nx] = cnt
                if not check:
                    maps[ny][nx] = 0
                    check = True
                else:
                    maps[ny][nx] = 2


            queue.append(tmp)
                
    bfs(0, 0)

    if board[n-1][n-1] == -1:
        answer = -1
    else:
        answer = board[n-1][n-1] 

    return answer

map1 = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]
        ] # 11
map2 = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,0],
        [0,0,0,0,1]
        ] # -1

print(solution(map1))
print(solution(map2))