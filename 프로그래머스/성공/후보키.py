from collections import deque

def solution(relation):
    answer = list()
    deq = deque([[i for i in range(len(relation[0]))]])

    result = list()

    while deq:
        target = deq.popleft()

        for i in range(len(target)):
            t = target.copy()
            t.remove(t[i])

            if t in result:
                continue

            keyList = list()

            for num in range(len(relation)):

                string = ''

                for j in t:
                    string += relation[num][j]
                keyList.append(string)
            if len(set(keyList)) == len(keyList):
                deq.append(t)
                result.append(t)
    # result = sorted(result, key=lambda x : len(x), reverse=True)

    # result = [''.join([str(j) for j in i]) for i in result]
    
    result = [set(i) for i in result]
    
    while result:
        target = result.pop()
        check = True
        if not answer:
            answer.append(target)
            continue
    
        for i in answer:
            if i & target == i:
                check = False
                break
        if check:
            answer.append(target)
    if not answer:
        return 1

    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	))
print(solution(	[["a", "1", "aaa", "c", "ng"], ["a", "1", "bbb", "e", "g"], ["c", "1", "aaa", "d", "ng"], ["d", "2", "bbb", "d", "ng"]]))