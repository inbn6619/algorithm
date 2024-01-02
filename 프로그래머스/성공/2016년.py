def solution(a, b):
    
    array = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    result = sum(array[:a])
    
    date = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    
    print(result)
                  
    result = result  - array[a - 1]
    
    print(result)
    
    result += b + 5
    
    print(result)
    
    result %= 7
    
    print(result)

    # print(date[result])
    
    answer = date[result-1]
    return answer