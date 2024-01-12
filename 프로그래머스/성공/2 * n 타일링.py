def solution(n):
    
    # 1과 2로 N을 만들 수 있는 경우의 수 구하라
    # 0 = 0, 1 = 1, 2 = 2, 3 = 3, 4 = 5, 5 = 8
    
    # dp[i] = (dp[i-1] + dp[i-2]) % 1000000007 // 정수 오버플로우 예방 코드
    # answer = dp[n] % 1000000007 보다 더 빠름

    
    dp = [0] * (n+1)
    
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    
    answer = dp[n]
    
    
    return answer