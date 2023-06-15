N = int(input())

# 0 1 2
# 3 4 5
# 6 7 8

matrix = [list(map(int, input().split())) for _ in range(N)]

result = list()

def divde_squ(y, x, N):
    color = matrix[y][x]

    for a in range(y, y + N):
        for b in range(x, x + N):
            if color != matrix[a][b]:
                div = N//3
                divde_squ(y, x, div) # 0분면
                divde_squ(y, x + div, div) # 1분면
                divde_squ(y, x + div*2, div) # 2분면
                divde_squ(y + div, x, div) # 3분면
                divde_squ(y + div, x + div, div) # 4분면
                divde_squ(y + div, x + div * 2, div) # 5분면
                divde_squ(y + div * 2, x, div) # 6분면
                divde_squ(y + div * 2, x + div, div) # 7분면
                divde_squ(y + div * 2, x + div * 2, div) # 8분면
                return

    if color == 0:
        result.append(0)
    elif color == 1:
        result.append(1)
    else:
        result.append(-1)

divde_squ(0, 0, N)

print(result.count(-1))
print(result.count(0))
print(result.count(1))