def solution(sequence, k):
    answer = []
    
    start, end = 0, 0
    
    result = sequence[0]
    
    while len(sequence) > end and len(sequence) > start:
        if result < k:
            end += 1
            if end == len(sequence):
                break
            result += sequence[end]
        else:
            if result == k:
                answer.append([start, end])
            result -= sequence[start]
            start += 1


    return sorted(answer, key=lambda x : (x[1]-x[0] + 1, x[0]))[0]

print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2]	, 6))