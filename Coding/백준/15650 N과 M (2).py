# N, M = map(int, input().split())

# ans = list()

# visited = list()

# def back():
#     if len(ans) == M and set(ans) not in visited:
#         print(' '.join(str(i) for i in ans))
#         arr = set(ans)
#         visited.append(arr)
        
    
#     for i in range(1, N + 1):
#         if i not in ans:
#             ans.append(i)
#             back()
#             ans.pop()

# back()


n,m = map(int, input().split())
s = []

def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in range(start, n+1):
        s.append(i)
        dfs(i+1)
        s.pop()

dfs(1)