N, M = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

ans = list()

def back():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return

    for i in array:
        ans.append(i)
        back()
        ans.pop()

back()