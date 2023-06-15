def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        i, j, k = i-1, j, k-1
        
        lst = sorted(array[i:j])

        answer.append(lst.pop(k))

    return answer

array1 = [1, 5, 2, 6, 3, 7, 4]
commands1 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(array1, commands1)