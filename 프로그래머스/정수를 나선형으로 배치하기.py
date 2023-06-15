def solution(n):
    matrix = [[0]*n for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]


    def snail(y, x, length, number):
        if length % 2 == 0:
            if length == 0:
                matrix[y][x] = number
                return
        else:
            if length < 0:
                return
        for i in range(4):
            for j in range(length):
                matrix[y][x] = number
                y += dy[i]
                x += dx[i]
                number += 1
        snail(y + 1, x + 1, length - 2, number)

    snail(0, 0, n-1, 1)

    answer = matrix
    return answer
    
solution(4)
solution(5)