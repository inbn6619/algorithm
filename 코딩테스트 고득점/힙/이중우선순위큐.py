def solution(operations):
    import heapq as hp
    answer = []
    min_heap = []
    max_heap = []

    for i in operations:
        s, num = i.split()
        num = int(num)

        if s == "I":
            hp.heappush(min_heap, num)
            hp.heappush(max_heap, -num)
        else:
            if min_heap:
                if num == -1:
                    hp.heappop(min_heap)
                    max_heap.pop()
                else:
                    hp.heappop(max_heap)
                    min_heap.pop()

    if min_heap:
        answer = [-(max_heap[0]), min_heap[0]]
    else:
        answer = [0, 0]

    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])) # [0, 0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])) # [333, -45]