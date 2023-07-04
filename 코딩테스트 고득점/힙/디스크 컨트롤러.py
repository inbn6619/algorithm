def solution(jobs): # jobs[0] = (a, b) # a == 시작 시간, b != end b == 작업 소요 시간
    from heapq import heappush, heappop
    answer, now, i = 0, 0, 0
    num = len(jobs)
    start = -1
    heap = []

    while i < num:
        for s, t in jobs:
            if start < s <= now:
                heappush(heap, [t, s])
        if len(heap) > 0:
            t, s = heappop(heap)
            start = now
            now += t
            answer += now - s
            i += 1
        else:
            now += 1

    return answer // num


print(solution([[0, 3], [10, 1]])) # 2 // 4
print(solution([[0, 3], [2, 6], [1, 9]])) # 9 // 27
print(solution([[7, 8], [3, 5], [9, 6]])) # 9 // 27
print(solution([[1, 4], [7, 9], [1000, 3]])) # 5 // 16
print(solution([[0, 1], [2, 2], [2, 3]])) # 2 // 8
print(solution([[0, 1], [2, 16], [3, 1]])) # 6 or 11 // 20 or 33