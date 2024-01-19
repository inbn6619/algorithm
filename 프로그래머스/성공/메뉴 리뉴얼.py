
def solution(orders, course):
    answer = []

    from collections import Counter
    from itertools import combinations
    
    # orders안의 원소에 대응하는 문자열 조합(set) 생성
    # 생성 방법 : BFS or DFS 사용 // 실패 (시간 초과)
    # 생성 방법 : itertools 안의 combinations 사용

    for c in course:
        result = list()
        for o in orders:
            result += [''.join(com) for com in combinations(sorted(o), c)]
        counter = Counter(result)
        if counter:
            maxValue = max(counter.values())

            appendResult = [key for key, value in counter.items() if value == maxValue and value >= 2]

            answer.extend(appendResult)

    return sorted(answer)
