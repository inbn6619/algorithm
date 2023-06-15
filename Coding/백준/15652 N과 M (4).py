N, M = map(int, input().split())

ans = list()

def back(V):
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(V, N + 1):
        ans.append(i)
        back(i)
        ans.pop()

back(1)