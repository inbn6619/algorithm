def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    def check(array, answers):
        num = len(answers)
        array = array * num
        answer = array[:num] 

        cnt = 0

        for i in range(num):
            if answer[i] == answers[i]:
                cnt += 1

        return cnt
    
    result = list()
    answer = []

    result.append(check(one, answers))
    result.append(check(two, answers))
    result.append(check(three, answers))

    if result.count(max(result)) == 3:
        answer = [1, 2, 3]
    elif result.count(max(result)) == 2:
        for i in range(len(result)):
            if result[i] == max(result):
                answer.append(i+1)
    else:
        answer = [result.index(max(result)) + 1]

    return answer

# solution([1,2,3,4,5])
# solution([1,3,2,4,2])
solution([1,2,2,5,2])