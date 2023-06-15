import sys

input = sys.stdin.readline

N, M = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

ans = list()
visited = [False] * N
sets = list()

def back(start):
    if len(ans) == M and ans not in sets:
        print(' '.join(map(str, ans)))
        sets.append(ans.copy())
        return
    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            num = array[i]
            ans.append(num)
            back(i)
            visited[i] = False
            ans.pop()

back(0)