from collections import deque

def solution(rectangle, cx, cy, ix, iy):
    answer = 0
    maxX = 0
    maxY = 0

    for x,y,x2,y2 in rectangle:
        maxX = max(x2 * 2,maxX)
        maxY = max(y2 * 2,maxY)

    graph = [[0] * (maxX + 2) for _ in range(maxY + 2)]

    #1로 안쪽 다 칠하고
    for x,y,x2,y2 in rectangle:
        for i in range((x * 2),(x2 * 2) + 1):
            for j in range((y * 2),(y2 * 2) + 1):
                graph[j][i] = 1

    #전체 돌면서 주위 8개중에 하나가 0이면서 자기 자신이 1이면 2로 바꿈 테두리 경로
    for y in range(1,maxY + 1):
        for x in range(1,maxX + 1):
            for i in range(3):
                for j in range(3):
                    if graph[y + i - 1][x + j - 1] == 0 and graph[y][x] == 1:
                        graph[y][x] = 2
                        break

    dx = [1,0, 0, -1]
    dy = [0,1, -1, 0]
    queue = deque([(cx * 2,cy * 2,0)])
    ix *= 2
    iy *= 2
    while queue:
        x, y,length = queue.popleft()
        graph[y][x] = 1
        if x == ix and y == iy:
            answer = (length // 2)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if graph[ny][nx] == 2:
                queue.append((nx,ny,length + 1))


    return answer
    

rectangle1 = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
rectangle2 = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
rectangle3 = [[1,1,5,7]]
rectangle4 = [[2,1,7,5],[6,4,10,10]]
rectangle5 = [[2,2,5,5],[1,3,6,4],[3,1,4,6]]

# print(solution(rectangle1, 1, 3, 7, 8)) # 17
print(solution(rectangle2, 9, 7, 6, 1)) # 11 
# print(solution(rectangle3, 1, 1, 4, 7)) # 9
# print(solution(rectangle4, 3, 1, 7, 10)) # 15
# print(solution(rectangle5, 1, 4, 6, 3)) # 10 