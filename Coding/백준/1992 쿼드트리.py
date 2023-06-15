N = int(input())

image = [[int(i) for i in list(input())] for _ in range(N)]

def div_img(y, x, n):
    color = image[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if color != image[i][j]:
                color = -1
                break
    if color == -1:
        div = n // 2
        print("(", end='')
        div_img(y, x, div)
        div_img(y, x + div, div)
        div_img(y + div, x, div)
        div_img(y + div, x + div, div)
        print(")", end="")

    elif color == 1:
        print(1, end='')
    else:
        print(0, end='')


div_img(0, 0, N)

# [110(0101), (0010), 1, (0001)]