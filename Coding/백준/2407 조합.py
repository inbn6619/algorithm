def factor(num):
    if num > 1:
        return num * factor(num -1)
    else:
        return 1
    
def permut(n, m):
    if m != 0:
        return n * permut(n-1, m-1)
    else:
        return 1

def combie(n, m):
    print(permut(n, m) // factor(m))

N, M = map(int, input().split())

combie(N, M)
