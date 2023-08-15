def solution(n, lost, reserve):
    temp = list()
    for l in lost:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)

    lost.sort()
    reserve.sort()

    while True:
        if not lost:
            break
        a = lost.pop(0)
        check = False

        for i in range(len(reserve)):
            if a - 1 <= reserve[i] <= a + 1:
                check = True
                reserve.pop(i)
                break

        if not check:
            temp.append(a)



    answer = n - len(temp)
    return answer


# print(solution(5, [2, 4], [1, 3, 5]))
# print(solution(5, [2,4], [3]))
# print(solution(3, [3], [1]))
# print(solution(4, [2, 3], [3, 4]))
print(solution(5, [4,2], [3, 5]))