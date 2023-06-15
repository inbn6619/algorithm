def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[:query[i] + 1]
        else:
            arr = arr[query[i] :]

    answer = arr
    return answer

arr1 = [0, 1, 2, 3, 4, 5]	
query1 = [4, 1, 2]

solution(arr1, query1)