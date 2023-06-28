def solution(game_board, table):
    from collections import deque

    n = len(game_board)
    table_coor = list()
    board_coor = list()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    

    def rotate(array):
        num = len(array)
        m = len(array[0])
        result = [[0] * num for _ in range(m)]
        for i in range(m):
            for j in range(num -1, -1, -1):
                result[i][j] = array[num-1 -j][i]
        return result
    
    table_R = rotate(table)
    table_L = rotate(rotate(table_R))

    def bfs(start, board, T, F, n, m):
        queue = deque([start])
        coor = list()
        coor.append(start)

        while queue:
            y, x = queue.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < m and 0 <= ny < n and board[ny][nx] == T:
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
                    coors.append(bfs([i, j], tab, 1, 0, len(tab), len(tab[0])))
                    
        table_coor.append(coors)


    for a in range(n):
        for b in range(n):
            if game_board[a][b] == 0:
                game_board[a][b] = 1
                board_coor.append(bfs([a, b], game_board, 0, 1, len(game_board), len(game_board[0])))

    def func(array):
        y, x = list(), list()
        for coor in array:
            x.append(coor[1])
            y.append(coor[0])

        square = [[0] * (max(x) - min(x) + 1) for _ in range(max(y) - min(y) + 1)]

        for coor in array:
            coor[1] -= min(x)
            coor[0] -= min(y)
            square[coor[0]][coor[1]] = 1

        return square

    board_square = list()
    table_square = [[0] * len(table_coor[0]) for _ in range(len(table_coor))]

    for b_coor in board_coor:
        board_square.append(func(b_coor))
    table, tables = table_coor[0], table_coor[1:]

    table_square[0] = [func(i) for i in table]

    for tab in range(1, len(tables) + 1):
        for t_coor in tables[tab -1]:
            square = func(t_coor)
            if rotate(square) in table_square[0]:
                table_square[tab][table_square[0].index(rotate(square))] = square
            else:
                table_square[tab][table_square[0].index(rotate(rotate(rotate(square))))] = rotate(rotate(rotate(square)))

    board_check = [False] * len(board_square)
    table_check = [False] * len(table_square[0])

    def dfs(board, table, num, visited):
        for i in range(len(table)):
            if not table_check[i]:
                target = board.copy()
                array = table.copy()
                for a in range(len(array[i])):
                    for b in range(len(array[i][0])):
                        if array[i][a][b] == 1:
                            stack = [bfs([a,b], array[i], 1, 0, len(array[i]), len(array[i][0]))[0]]
                visited.append(i)
                Check = True

                while stack:
                    y, x = stack.pop()
                
                    for j in range(4):
                        nx = dx[j] + x
                        ny = dy[j] + y

                        if 0 <= nx < len(array[i][0]) and 0 <= ny < len(array[i]):
                            if (target[ny][nx] == 1 and array[i][ny][nx] == 1):
                                target[ny][nx] = 0
                                array[i][ny][nx] = 0
                            elif target[ny][nx] == 1 or array[i][ny][nx] == 1:
                                Check = False
                                visited.pop()
                                break
                if Check:
                    # 여기서 target 안의 1 좌료 추출 후 해당 좌표로 func 돌려서 target 갱신해주고
                    new_board = list()
                    for i in range(len(target)):
                        for j in range(len(target[0])):
                            if target[i][j] == 1:
                                new_board = func(bfs([i,j], target, 1, 0, len(target), len(target[0])))
                                
                    

                    # 갱신된 값을 가지고 dfs 한번 들어가주고 target이 전부 0일 경우 checklist[i]에 visited 사용해서 갱신해주면됨

                    
                



    visited = list()
    
    for i in range(len(board_square)):
        for square in table_square:
            for j in range(len(square)):
                if not board_check[i] and not table_check[j]:
                    if board_square[i] == square[j]:
                        board_check[i] = True
                        table_check[j] = True
                    else:
                        dfs(board_square[i], square, i, visited)




    answer = -1
    return answer

game_board1 = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
game_board2 = [[0,0,0],[1,1,0],[1,1,1]]
table1 = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
table2 = [[1,1,1],[1,0,0],[0,0,0]]

print(solution(game_board1, table1))
print(solution(game_board2, table2))