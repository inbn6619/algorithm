def solution(maps):

    width = len(maps)
    height = len(maps[0])

    answer = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    board = [[0] * width for _ in range(height)]
    
    def bfs(x, y):


    return answer

map1 = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]
        ] # 11
map2 = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,0],
        [0,0,0,0,1]
        ] # -1

print(solution(map1))
print(solution(map2))