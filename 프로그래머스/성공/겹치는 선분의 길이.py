# 3개의 집합의 교집합의 요소 갯수 구하기

Tline = [[0, 2], [-3, -1], [-2, 1]] # 2
line1 = [[0, 1], [2, 5], [3, 9]] # 2
line2 = [[-1, 1], [1, 3], [3, 9]] # 0
line3 = [[0, 5], [3, 9], [1, 10]] # 8

def solution(lines):

    for i in range(len(lines)):
        lines[i] = [int(s) for s in range(lines[i][0], lines[i][1])]

    set1, set2, set3 = map(set, lines)
    
    answer = len((set1 & set2 & set3) | (set1 & set2) | (set1 & set3) | (set2 & set3))
    return answer

solution(Tline)
solution(line1)
solution(line2)
solution(line3)

print()