board1 = [
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0]] # 16
board2 = [
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 0]] # 13
board3 = [
    [1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1]] # 0

def solution(board):

    ix = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    iy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

    n = len(board)

    coordinate = list()

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                coordinate.append([i, j])

    for coor in coordinate:
        y, x = coor

        for t in range(9):
            nx = ix[t] + x
            ny = iy[t] + y

            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == 1:
                    pass
                else:
                    board[ny][nx] = 1


    answer = n**2 - sum([sum(i) for i in board])
    return answer

solution(board1)
solution(board2)
solution(board3)