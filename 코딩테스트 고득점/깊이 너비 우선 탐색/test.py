def solution(game_board, table):
    from collections import deque
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
    
    def bfs(start, array, T, F, heigth, width):
        queue = deque([start])
        coor = [start]

        while queue:
            y, x = queue.popleft()

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < width and 0 <= ny < heigth and array[ny][nx] == T:
                    queue.append([ny, nx])
                    array[ny][nx] = F
                    coor.append([ny, nx])

        return coor

    game_coor = list()
    table_coor = list()
    table = [table] + [rotate(table)] + [rotate(rotate(table))] + [rotate(rotate(rotate(table)))] 

    num = len(game_board)

    for i in range(num):
        for j in range(num):
            if game_board[i][j] == 0:
                game_coor.append(bfs([i,j], game_board, 0, 1, num, num))

    for t in range(4):
        for i in range(num):
            for j in range(num):
                if table[t][i][j] == 1:
                    table_coor.append(bfs([i, j], table[t], 1, 0, num, num))
            


    def func(array):
        y = list()
        x = list()

        for coor in array:
            x.append(coor[1])
            y.append(coor[0])
        
        square = [[0] * (max(x) - min(x) + 1) for _ in range(max(y) - min(y) + 1)]

        for i in range(len(array)):
            square[array[i][0]-min(y)][array[i][1]-min(x)] = 1
        
        return square

    game_square = list()
    table_square = list()

    for coor in table_coor:
        table_square.append(func(coor))

    for coor in game_coor:
        game_square.append(func(coor))


    
    game_check = [False] * len(game_square)
    # table_check = [False] * len(table_square)

    # for i in range(len(game_square)):
    #     for t in range(4):
    #         for j in range(len(table_square)):
    #             if not game_check[i] and not table_check[j]:
    #                 if game_square[i] == table_square[j]:
    #                     game_check[i] = True
    #                     table_check[j] = True
    #         table_square = rotate(table_square)

    for i in range(len(game_square)):
        for t in range(4):
            for j in range(len(table_square)):
                if not game_check[i]:
                    if game_square[i] == table_square[j]:
                        game_check[i] = True

    count = 0

    for i in range(len(game_square)):
        if game_check[i]:
            for j in range(len(game_square[i])):
                count += sum(game_square[i][j])



    answer = count
    return answer


game_board1 = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
game_board2 = [[0,0,0],[1,1,0],[1,1,1]]
table1 = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
table2 = [[1,1,1],[1,0,0],[0,0,0]]

game_board3 = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]

table3 = [[0, 1, 0], [1, 1, 1], [1, 0, 1]]

game_board4 = [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

table4 = [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]

print(solution(game_board1, table1))
# print(solution(game_board2, table2))
# print(solution(game_board3, table3))
# print(solution(game_board4, table4)) # 54