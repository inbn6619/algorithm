def solution(array):
    setlist = set(array)

    result = dict()

    for i in setlist:
        result[i] = array.count(i)

    res = list(result.values())
    res.sort()

    if res.count(max(res)) == 1:
        answer = [k for k, v in result.items() if v == max(res)][0]
    else:
        answer = -1
    return answer

array1 = [1, 2, 3, 3, 3, 4]
array2 = [1, 1, 2, 2]
array3 = [1]

print(solution(array1))
print(solution(array2))
print(solution(array3))