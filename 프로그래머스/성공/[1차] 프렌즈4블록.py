def solution(m, n, board):

    answer = 0

    board = [list(i) for i in board]
        
    dx = [1, 0, 1]
    dy = [0, 1, 1]

    
    
    def check(y, x, target):

        for i in range(3):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<= nx < n and 0<= ny < m:
                if checkMatrix[ny][nx] == 0 and target == board[ny][nx]:
                    checkMatrix[ny][nx] = 1
                    check(ny, nx, target)

        cnt = 0

        for i in range(3):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<= nx < n and 0<= ny < m:
                if checkMatrix[ny][nx] == 1 and target == board[ny][nx]:
                    cnt += 1
        if cnt == 3:
            for i in range(3):
                nx = dx[i] + x
                ny = dy[i] + y
                answerSet.add((ny, nx))
            answerSet.add((y, x))
            
    boolean = True
    while boolean:

        checkMatrix = [[0] * n for i in range(m)]

        answerSet = set()

        boolean = False
        for i in range(m):
            for j in range(n):                
                if checkMatrix[i][j] == 0 and board[i][j] != "X":
                    checkMatrix[i][j] = 1
                    check(i, j, board[i][j])

        if len(answerSet) > 0:
            answer += len(answerSet)

            boolean = True

            for y, x in answerSet:
                board[y][x] = "X"

        for i in range(m-1, -1, -1):
            for j in range(n):
                if board[i][j] == "X":
                    t = i
                    c = t

                    while i >= 0:
                        if board[i][j] != "X":
                            board[c][j], board[i][j] = board[i][j], board[c][j]
                            c -= 1
                        else:
                            i -= 1
                    i = t

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]	))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	))