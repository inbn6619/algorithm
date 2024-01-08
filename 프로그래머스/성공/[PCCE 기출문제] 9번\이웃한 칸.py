def solution(board, h, w):
    answer = 0
    
    target = board[h][w]
    
    dx = [1, 0, 0, -1]
    
    dy = [0, 1, -1 ,0]
    
    w_check = len(board[0])
    h_check = len(board)
    
    for i in range(4):
        nx = w + dx[i]
        ny = h + dy[i]
        
        if 0<= nx < w_check and 0<= ny < h_check:
            if board[ny][nx] == target:
                answer += 1
            
    
    return answer