def solution(N, road, K):
    answer = 0
    
    INF = int(1e9)
    
    matrix = [[INF] * N for i in range(N)]
    
    
    for n, t, num in road:
        n -= 1
        t -= 1

        matrix[n][t] = min(num, matrix[n][t])
        matrix[t][n] = min(num, matrix[t][n])
        matrix[n][n] = 0
        matrix[t][t] = 0
        
        
    for k in range(N):
        for i in range(N):
            for j in range(N):
                matrix[i][j] = min(matrix[i][j], matrix[k][i] + matrix[j][k])
                
    for i in matrix[0]:
        if i <= K:
            answer += 1

#     for m in matrix:
#         print(m)



    return answer
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	, 3))