def solution(numbers, target):

    def dfs(idx, total):
        if idx == len(numbers):
            if total == target:
                nonlocal answer
                answer += 1
                return
        else:
            dfs(idx+1, total + numbers[idx])
            dfs(idx+1, total - numbers[idx])

    answer = 0
    dfs(0, 0)

    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))