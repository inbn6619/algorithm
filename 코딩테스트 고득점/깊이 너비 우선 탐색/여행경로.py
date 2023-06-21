def solution(tickets):
    result = list()

    def dfs(end):
        nonlocal cnt
        nonlocal check
        if cnt == len(tickets):
            result.append(path.copy())
            return

        for n in range(len(tickets)):
            if n not in idx and end == tickets[n][0]:
                path.append(tickets[n][1])
                idx.append(n)
                cnt += 1
                dfs(tickets[n][1])
                cnt -= 1
                path.pop()
                idx.pop()
        
        if check:
            result.append(path.copy())
            check = False

    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            cnt = 1
            path = tickets[i].copy()
            idx = [i]
            check = True
            dfs(tickets[i][1])


    Max_num = 0
    checklist = list()
    for lst in result:
        if len(lst) >= Max_num:
            Max_num = len(lst)

    for lst in result:
        if len(lst) == Max_num:
            checklist.append(lst)

    checklist.sort()
    answer = checklist[0]
    return answer

ticket1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
ticket2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
ticket3 = [['ICN', "ASD"], ["ASD", "DFS"]]
ticket4 = [['ICN', "ASD"], ["GDS", "DFS"]]



print(solution(ticket1))
print(solution(ticket2))
print(solution(ticket3))
print(solution(ticket4))