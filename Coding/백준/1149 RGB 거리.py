N = int(input()) # 집의 수

house = list()

for i in range(N):
    array = [int(i) for i in input().split()]
    house.append(array)

matrix = [[0]*3 for i in range(N)]

for i in range(N):
    if i == 0:
        matrix[i] = house[i]
    
    else:
        matrix[i][0] = house[i][0] + min(matrix[i-1][1], matrix[i-1][2])
        matrix[i][1] = house[i][1] + min(matrix[i-1][0], matrix[i-1][2])
        matrix[i][2] = house[i][2] + min(matrix[i-1][0], matrix[i-1][1])

print(min(matrix[-1]))