def solution(progresses, speeds):
    from collections import deque
    answer = []
    dates = deque()
    for i in range(len(progresses)):
        target = progresses[i]
        date = 0
        while target < 100:
            date += 1
            target += speeds[i]

        dates.append(date)

    cnt = 0
    check = 0
    while True:
        num = dates.popleft()

        if num < check:
            num = check

        cnt += 1

        if not dates:
            answer.append(cnt)
            break

        if num < dates[0]:
            answer.append(cnt)
            cnt = 0

        check = num

    return answer


progresses1 = [93, 30, 55]
progresses2 = [95, 90, 99, 99, 80, 99]
speeds1 = [1, 30, 5]
speeds2 = [1, 1, 1, 1, 1, 1]

print(solution(progresses1, speeds1))
print(solution(progresses2, speeds2))