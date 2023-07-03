def solution(scoville, K):
    import heapq as hp

    hp.heapify(scoville)
    answer = 0
    now = scoville[0]

    while now < K and len(scoville) > 1:
        first = hp.heappop(scoville)
        second = hp.heappop(scoville)
        new = first + second * 2
        hp.heappush(scoville, new)
        now = scoville[0]
        answer += 1

    if min(scoville) < K:
        answer = - 1


    return answer


print(solution([1, 2], 2))