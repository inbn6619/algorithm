
def solution(rectangle, characterX, characterY, itemX, itemY):

    mx = 0
    my = 0

    for x1, y1, x2, y2 in rectangle:
        mx = max([mx, x2])
        my = max([my, y2])

    m = max([my, mx]) + 2
 
    board = [[0] * m for _ in range(m)]


    for x1, y1, x2, y2 in rectangle:
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                board[i][j] = 1

    ox = [-1, 0, 1, -1, 1, -1, 0, 1]
    oy = [1, 1, 1, 0, 0, -1, -1, -1]

    def border(y, x):
        for n in range(8):
            nx = ox[n] + x
            ny = oy[n] + y

            if 0 <= nx < m and 0 <= ny < m and board[ny][nx] == 1:
                board[ny][nx] = 2

    for i in range(m):
        for j in range(m):
            if board[i][j] == 0:
                border(i, j)





    # def bfs(cy, cx, iy, ix):
    #     from collections import deque
    #     queue = deque([[cy, cx]])

    #     dx = [1, 0, -1, 0]
    #     dy = [0, 1, 0, -1]

    #     while queue:
    #         y, x = queue.popleft()

    #         for f in range(4):
    #             new_x = dx[f] + x
    #             new_y = dy[f] + y

    #             if 0 <= new_x < m and 0 <= new_y < m and board[new_y][new_x] == 2:
    #                 board[new_y][new_x] = board[y][x] + 1
    #                 queue.append([new_y, new_x])

    #     return board[iy][ix]


    # answer = bfs(characterY, characterX, itemY, itemX)

    answer = 0
    return answer


rectangle1 = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
rectangle2 = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
rectangle3 = [[1,1,5,7]]
rectangle4 = [[2,1,7,5],[6,4,10,10]]
rectangle5 = [[2,2,5,5],[1,3,6,4],[3,1,4,6]]

# print(solution(rectangle1, 1, 3, 7, 8)) # 17
print(solution(rectangle2, 9, 7, 6, 1)) # 11 
# print(solution(rectangle3, 1, 1, 4, 7)) # 9
# print(solution(rectangle4, 3, 1, 7, 10)) # 15
# print(solution(rectangle5, 1, 4, 6, 3)) # 10 