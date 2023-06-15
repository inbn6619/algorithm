N, M = map(int, input().split())

res = list()

def back():
    if len(res) == M:
        print(' '.join(str(i) for i in res))
        return

    for i in range(1, N + 1):
        if i not in res:
            res.append(i)
            back()
            res.pop()

back()