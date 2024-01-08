def solution(board, moves):
    answer = 0
    
    stackList = [[] for _ in range(len(board))]
        
    for i in range(len(board) -1, -1, -1):
        for j in range(len(board)):
            if board[i][j] != 0:
                stackList[j].append(board[i][j])
                
    bucket = [0]
                
    for m in moves:
        m -= 1
                
        if stackList[m]:
            selected = stackList[m].pop()

            if bucket[-1] == selected:
                bucket.pop()
                answer += 2
            else:
                bucket.append(selected)

    return answer