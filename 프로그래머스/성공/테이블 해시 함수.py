def solution(data, col, row_begin, row_end):
    answer = 0

    sortedData = sorted(data, key=lambda x : (x[col-1], -x[0]))
        
    rows = zip(range(row_begin, row_end+1), sortedData[row_begin - 1: row_end])
    
    for idx, row in rows:
        result = 0
        
        for e in row:
            result += e % idx
        
        answer ^= result

    
    return answer