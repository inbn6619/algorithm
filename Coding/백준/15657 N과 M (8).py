N, M = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

ans = list()

def back(start):
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(start, N):
        num = array[i]
        ans.append(num)
        back(i)
        ans.pop()

back(0)