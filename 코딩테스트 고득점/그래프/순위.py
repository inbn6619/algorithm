from collections import Counter


# a 가 b를 이김
def solution(n, results):

    matrix = [[0] * n for _ in range(n)]

    for y, x in results:
        matrix[y-1][x-1] = 1
        matrix[x-1][y-1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    if matrix[i][k] == 1 and matrix[k][j] == 1:
                        matrix[i][j] = 1
                        matrix[j][i] = -1


    answer = 0

    # for arr in matrix:
    #     check = True
    #     for i in arr:
    #         if not i:
    #             check = False
    #             break
    #     if check:
    #         answer += 1

    for i in range(n):
        if Counter(matrix[i])[0] == 1:
            answer += 1

    return answer



print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))