def solution(tickets):
    result = list()


    def dfs(end):
        nonlocal cnt
        path.append(end)

        for i in range(len(tickets)):
            if tickets[i][0] == end and i not in idx:
                cnt += 1
                idx.append(i)
                dfs(tickets[i][1])

        if cnt == len(tickets):
            return
        
        path.pop()
        idx.pop()
                
    for n in range(len(tickets)):
        if tickets[n][0] =='ICN':
            idx = [n]
            path = [tickets[n][0]]
            cnt = 1
            dfs(tickets[n][1])
            result.append(path.copy())
    
    result.sort()
    answer = result[0]
    return answer



ticket1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
ticket2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(ticket1))
print(solution(ticket2))