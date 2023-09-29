def solution(numlist, n):
    answer = [abs(n-i) for i in numlist]

    leng = len(numlist)

    for i in range(leng - 1):
        for j in range(leng - 1 - i):
            if answer[j] == answer[j + 1]:
                if numlist[j] < numlist[j + 1]:
                    numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
            elif answer[j] > answer[j + 1]:
                answer[j], answer[j + 1] = answer[j + 1], answer[j]
                numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]

    answer = numlist
                
    return answer

numlist1 = [10000,20,36,47,40,6,10,7000]

print(solution(numlist1, 30))