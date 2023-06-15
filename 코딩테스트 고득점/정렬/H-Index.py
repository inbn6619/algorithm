def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            answer +=1

    return answer

print(solution([3, 0, 6, 1, 5]))
print(solution([1,1,0,2,3,1,1,1]))