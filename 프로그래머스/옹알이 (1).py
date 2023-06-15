def solution(babbling):
    checklist = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for word in babbling:
        for check in checklist:
            if check in word:
                word = word.replace(check, len(check) * ' ')
        if not word.strip():
            cnt += 1

    answer = cnt
    return answer

array1 = ["aya", "yee", "u", "maa", "wyeoo"]
array2 = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]	

result1 = solution(array1)
result2 = solution(array2)

print()