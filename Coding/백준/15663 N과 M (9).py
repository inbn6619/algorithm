import sys

input = sys.stdin.readline

N, M = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

ans = list()
visited = [False] * N

def back(dep):
    if dep == M:
        print(' '.join(map(str, ans)))
        return
    check = 0
    for i in range(N):
        if not visited[i] and check != array[i]:
            visited[i] = True
            ans.append(array[i])
            check = array[i]

            back(dep + 1)

            visited[i] = False
            ans.pop()

back(0)