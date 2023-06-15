N, M = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

ans = list()

visited = list()

def back(start):
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        visited.append(ans.copy())
        return
    
    check = 0

    for i in range(start, N):
        num = array[i]
        if check != num:
            ans.append(num)
            check = num
            back(0)
            ans.pop()

back(0)