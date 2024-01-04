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

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))