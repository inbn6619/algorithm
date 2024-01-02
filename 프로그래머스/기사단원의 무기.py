def solution(number, limit, power):
    answer = 0

    def counts(num):
        count = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                if i == num // i:
                    count += 1
                else:
                    count += 2
        return count


    numList = list()

    for i in range(1, number + 1):
        numList.append(counts(i))

    for j in numList:
        if j <= limit:
            answer += j
        else:
            answer += power


    return answer