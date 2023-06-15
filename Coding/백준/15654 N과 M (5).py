N, M = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

ans = list()

def back():
    if len(ans) == M:
        print(' '.join(str(i) for i in ans))
        return
    for i in array:
        if i not in ans:
            ans.append(i)
            back()
            ans.pop()

back()