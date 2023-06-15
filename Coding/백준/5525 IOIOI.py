N = int(input())
M = int(input())
S = input()

P = "IOI"

i = 0
ans = 0
cnt = 0

while i < M:
    if P == S[i:i + 3]:
        cnt += 1
        i += 2

        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        cnt = 0
        i += 1

print(ans)