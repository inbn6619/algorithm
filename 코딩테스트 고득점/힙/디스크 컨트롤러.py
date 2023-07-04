def solution(jobs): # jobs[0] = (a, b) # a == 시작 시간, b != end b == 작업 소요 시간
    import operator
    n = len(jobs)
    jobs = sorted(jobs, key=operator.itemgetter(0, 1))
    job = jobs.pop(0)
    now = sum(job)
    time = job[1]

    while jobs:
        time1 = 4000
        idx = 0
        num1 = 0
        num2 = 0
        for i, (s, t) in enumerate(jobs):
            if s > now:
                time2 = t
                num1 = s + t
            else:
                time2 = abs(now - s) + t
                num1 = now + t


            if time1 >= time2:
                time1 = time2
                idx = i
                num2 = num1

        now = num2
        time += time1
        jobs.pop(idx)

    answer = time // n

    return answer


# print(solution([[0, 3], [10, 1]])) # 2 // 4
# print(solution([[0, 3], [2, 6], [1, 9]])) # 9 // 27
# print(solution([[7, 8], [3, 5], [9, 6]])) # 9 // 27
# print(solution([[1, 4], [7, 9], [1000, 3]])) # 5 // 16
# print(solution([[0, 1], [2, 2], [2, 3]])) # 2 // 8
print(solution([[0, 1], [2, 16], [3, 1]])) # 6 or 11 // 20 or 33