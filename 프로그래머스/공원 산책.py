def solution(park, routes):
    answer = []

    def dfs(y, x, ranged):
        if not ranged:
            return [y, x]
        num = ranged.pop(0)
        way, length = routes[num].split(' ')
        length = int(length)
        ny, nx = y, x
        Xcheck = True

        
        for i in range(length):

            if way == 'E' or way == 'S':
                if way == 'E':
                    nx += 1
                else:
                    ny += 1
            else:
                if way == 'W':
                    nx -= 1
                else:
                    ny -= 1

            if 0 <= ny < height and 0 <= nx < width:    
                if park[ny][nx] == 'X':
                    Xcheck = False
                    break
            else:
                Xcheck = False
                break
        if Xcheck:
            y, x = ny, nx
                
        return dfs(y, x, ranged)


    height = len(park)
    width = len(park[0])

    check = True

    for h in range(height):
        for w in range(width):
            if park[h][w] == 'S':
                answer = dfs(h, w, [int(i) for i in range(len(routes))])
                check = False
                break
        if not check:
            break

    return answer

park1 = ["OSO","OOO","OXO","OOO"]
routes1 = ["E 2","S 3","W 1"]

solution(park1, routes1)