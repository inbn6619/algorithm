N, M = map(int, input().split())

ans = list()

def back():
    if len(ans) == M:
        print(' '.join(str(i) for i in ans))
        return
    for i in range(1, N + 1):
        ans.append(i)
        back()
        ans.pop()

back()