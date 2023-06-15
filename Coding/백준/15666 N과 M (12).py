N, M = map(int, input().split())

array = list(map(int, input().split()))

array = sorted(set(array))

ans = list()

def back(start):
    if len(ans) == M :
        print(' '.join(map(str, ans)))
        return    

    for i in range(start, len(array)):
        ans.append(array[i])
        back(i)
        ans.pop()

back(0)

