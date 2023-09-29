import functools
import sys
sys.setrecursionlimit(500000)
@functools.lru_cache(maxsize=None)

def solution(n):
    dp = [0, 1]
    def fib(n):
        if n == 2:
            dp.append(dp[0] + dp[1])
        else:
            fib(n-1)
            dp.append(dp[-1] + dp[-2])
    if n >= 2:
        fib(n)
    answer = dp[n]
    return answer % 1234567

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))