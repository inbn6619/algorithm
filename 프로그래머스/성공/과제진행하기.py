from collections import deque

def solution(plans):
    
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plans[i][2])
        
    # print(plans)
    
    sortedPlans = sorted(plans, key=lambda x : x[1])
    
    # print(sortedPlans)
    
    stack = list()
    
    plan = deque(sortedPlans)
    
    nextTime = sortedPlans[0][1]
    
    answer = []

    while plan:
        n, st, t = plan.popleft()
                
        if plan:
            nextTime = plan[0][1]
        
        time = nextTime - st

        if time == 0:
            answer.append(n)
            while stack:
                answer.append(stack.pop()[0])
            break
        
        time -= t
        
        if time < 0:
            stack.append([n, -(time)])
        else:
            answer.append(n)
            while time > 0:
                if stack:
                    target = stack[-1][-1]
                    target -= time
                    if target <= 0:
                        time = -(target)
                        answer.append(stack.pop()[0])
                        if target == 0:
                            break
                    else:
                        stack[-1][-1] = target
                        time = 0
                else:
                    break

    return answer


# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]	))
# print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]	))
# print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]	))
print(solution([["1", "00:00", "30"], ["2", "00:10", "40"], ["3", "00:20", "10"], ["4", "00:25", "10"], ["5", "01:10", "10"]])) # ["4","3","2","5","1"]
print(solution(	[["a", "09:00", "30"], ["b", "09:10", "20"], ["c", "09:15", "20"], ["d", "09:55", "10"], ["e", "10:50", "5"]])) # ["c", "b", "d", "a", "e"]