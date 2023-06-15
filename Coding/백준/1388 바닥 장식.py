# - 같은 행 ---- = 1, -- = 1, --|- = 2
# | 같은 열 [[--||], [---|]] == 2

def Wdfs(x, y):
    if 0 <= y < M:
        if matrix[x][y] == '-':
            matrix[x][y] = 0
            Wdfs(x, y + 1)

def Hdfs(x, y):
    if 0 <= x < N:
        if matrix[x][y] == '|':
            matrix[x][y] = 0
            Hdfs(x + 1, y)

N, M = map(int, input().split())

matrix = [list(input()) for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] == '-':
            Wdfs(i, j)
            cnt += 1
        elif matrix[i][j] == '|':
            Hdfs(i, j)
            cnt += 1

print(cnt)