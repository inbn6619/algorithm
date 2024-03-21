from collections import deque

def solution(users, emoticons):
    answer = []

    checkList = [0 for _ in range(len(emoticons))]
    
    # print(checkList)
    
    oneTenthValues = [i / 100 for i in emoticons]
    
    queue = deque([checkList])

    checkSet = set()
    checkSet.add(tuple(checkList))
    
    while queue:
        check = queue.popleft()

        memberships = 0

        payments = 0

        for j in range(len(check)):
            if check[j] < 40:
                check[j] += 10
                tupleCheck = tuple(check)

                if tupleCheck not in checkSet:
                    checkSet.add(tupleCheck)
                    queue.append(check.copy())
                check[j] -= 10


        for r, m in users:
            money = 0
            for i in range(len(check)):
                if check[i] >= r:
                    money += emoticons[i] - (oneTenthValues[i] * check[i])

            if m <= money:
                memberships += 1
            else:
                payments += money

        if memberships:
            answer.append([memberships, int(payments)])

    if answer:
        answer = sorted(answer, key=lambda x: (x[0], x[1]), reverse=True)

        return answer[0]
    else:
        return [0, 0]


# print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
# print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))

users = [[20, 5000], [30, 7000]]
emoticons = [3000, 4000]

print(solution(users, emoticons))

users = [[50, 1000], [60, 2000]]
emoticons = [500, 600]

print(solution(users, emoticons))
