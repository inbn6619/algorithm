def solution(rectangle, characterX, characterY, itemX, itemY):
    max_x = 0
    max_y = 0

    for x1, y1, x2, y2 in rectangle:
        max_x = max([x1, x2, max_x])
        max_y = max([y1, y2, max_y])
    
    max_corr = max([max_x, max_y]) + 1

    board = [[0] * (max_corr) for _ in range(max_corr)]

    def make_square(x1, y1, x2, y2):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 1:
                    continue
                if (y in [y1, y2] and x1 <= x <= x2 ) or (x in [x1, x2] and y1 <= y <= y2):
                    board[y][x] = 1

    for x1, y1, x2, y2 in rectangle:
        make_square(x1, y1, x2, y2)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def bfs(start, end):
        from collections import deque

        queue = deque([start])
        # board[start[1]][start[0]] = "start"

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < max_corr and 0 <= ny < max_corr and board[ny][nx] == 1:
                    board[ny][nx] = board[y][x] + 1
                    queue.append([nx, ny])
        
    bfs([characterX, characterY], [itemX, itemY])


    answer = 0
    return answer   

rectangle1 = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
rectangle2 = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
rectangle3 = [[1,1,5,7]]
rectangle4 = [[2,1,7,5],[6,4,10,10]]
rectangle5 = [[2,2,5,5],[1,3,6,4],[3,1,4,6]]

print(solution(rectangle1, 1, 3, 7, 8)) # 17
print(solution(rectangle2, 9, 7, 6, 1)) # 11 
print(solution(rectangle3, 1, 1, 4, 7)) # 9
print(solution(rectangle4, 3, 1, 7, 10)) # 15
print(solution(rectangle5, 1, 4, 6, 3)) # 10 