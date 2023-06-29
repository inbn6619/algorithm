def solution(arr):
    from collections import deque
    queue = deque(arr)
    answer = []

    while True:
        num = queue.popleft()

        if not queue:
            answer.append(num)
            break

        if queue[0] != num:
            answer.append(num)

    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))