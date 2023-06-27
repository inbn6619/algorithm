def solution(game_board, table):
    from collections import deque

    n = len(game_board)
    table_coor = list()
    board_coor = list()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    

    def rotate(array):
        num = len(array)
        result = [[0] * num for _ in range(num)]
        for i in range(num):
            for j in range(num -1, -1, -1):
                result[i][j] = array[num-1 -j][i]
        return result
    
    table_R = rotate(table)
    table_L = rotate(rotate(table_R))

    def bfs(start, board, T, F):
        queue = deque([start])
        coor = list()
        coor.append(start)

        while queue:
            y, x = queue.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == T:
                    coor.append([ny, nx])
                    queue.append([ny, nx])
                    board[ny][nx] = F

        return coor

    for tab in [table, table_R, table_L]:
        coors = list()
        for i in range(n):
            for j in range(n):
                if tab[i][j] == 1:
                    tab[i][j] = 0
                    coors.append(bfs([i, j], tab, 1, 0))
                    
        table_coor.append(coors)


    for a in range(n):
        for b in range(n):
            if game_board[a][b] == 0:
                game_board[a][b] = 1
                board_coor.append(bfs([a, b], game_board, 0, 1))

    def func(array):
        y, x = list(), list()
        for coor in array:
            x.append(coor[1])
            y.append(coor[0])
        
        min_x = min(x)
        min_y = min(y)

        for coor in array:
            coor[1] -= min_x
            coor[0] -= min_y


    for b_coor in board_coor:
        func(b_coor)
    for t in table_coor:
        for t_coor in t:
            func(t_coor)                

    answer = -1
    return answer

game_board1 = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
game_board2 = [[0,0,0],[1,1,0],[1,1,1]]
table1 = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
table2 = [[1,1,1],[1,0,0],[0,0,0]]

print(solution(game_board1, table1))
print(solution(game_board2, table2))