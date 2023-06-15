# 재귀 사용해서 전체 > 4분 > 16분 방향으로 함수 만들기
# N을 입력 받고 4분할 하고 연산
# 0 1
# 2 3


N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

result = list()

def div_squ(y, x, V):
    color = matrix[y][x]

    for i in range(y, V + y):
        for j in range(x, V + x):
            if color != matrix[i][j]:
                div = V//2
                div_squ(y, x, div)
                div_squ(y, x + div, div)
                div_squ(y + div, x, div)
                div_squ(y + div, x + div, div)
                return
    if color == 1:
        result.append(1)
    else:
        result.append(0)

div_squ(0, 0, N)

print(result.count(0))
print(result.count(1))