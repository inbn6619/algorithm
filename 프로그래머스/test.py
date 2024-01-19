def makeStringByStrElements(string):
    from collections import deque
    
    deq = deque(set(string[0]))
    
    print(deq)
    
    cnt = 0
    
    while deq:
        target = set(deq.popleft())
        print(target)
        
        for s in string:
            target.add(s)
            
            deq.append(target)  
        cnt += 1
        if cnt == 5:
            break


def solution(orders, course):
    answer = []
    
    # orders안의 원소에 대응하는 문자열 조합(set) 생성
    # 생성 방법 : BFS or DFS 사용, set 사용하여 시간복잡도 줄이기
    
    makeStringByStrElements(orders[0])

    
    return answer