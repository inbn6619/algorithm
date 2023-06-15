def solution(n, wires):

    answer = list()

    def dfs(num):
        nodes = [num]
        cnt = 0

        while nodes:
            node = nodes.pop()

            if not check[node]:
                check[node] = True
                nodes.extend(towers[node])
                cnt += 1
        return cnt

    for i in range(len(wires)):
        towers = [[] for _ in range(n+1)]
        check = [False for _ in range(n + 1)]
        wire = wires.copy()
        wire.pop(i)

        for start, end in wire:
            towers[start].append(end)
            towers[end].append(start)

        for num in range(1, len(towers)):
            if towers[num]:
                res = dfs(num)
                break
                
        answer.append(abs(res - (n - res)))
        
    return min(answer)


solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
solution(4, [[1,2],[2,3],[3,4]])
solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])