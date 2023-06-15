def merge(array):
    if len(array) < 2:
        return array
    mid = len(array)//2
    low_arr = merge(array[:mid])
    high_arr = merge(array[mid:])

    merged = []

    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if int(str(low_arr[l]) + str(high_arr[h])) < int(str(high_arr[h]) + str(low_arr[l])):
            merged.append(high_arr[h])
            h += 1
        else:
            merged.append(low_arr[l])
            l += 1
    
    merged += low_arr[l:]
    merged += high_arr[h:]
    return merged


def solution(numbers):
    answer = ''.join(str(i) for i in merge(numbers))

    if answer[0] == '0':
        answer = '0'

    return answer
solution([0, 0, 1, 0, 0])
solution([0, 0, 0, 1])
solution([0, 0, 0, 0])
solution([1, 10, 100, 1000])
solution([12, 1213])