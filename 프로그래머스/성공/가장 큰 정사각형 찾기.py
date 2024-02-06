def solution(board):
    answer = 0
    
    h = len(board)
    w = len(board[0])

    for i in range(1, h):
        for j in range(1, w):
            target = [board[i-1][j-1], board[i-1][j], board[i][j-1]]
            if board[i][j] == 1:
                board[i][j] = min(target) + 1
            
    answer = max([max(i) for i in board]) ** 2
    
    
    return answer