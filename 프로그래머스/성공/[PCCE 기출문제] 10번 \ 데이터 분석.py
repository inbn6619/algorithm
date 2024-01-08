def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    
    columns = ["code", "date", "maximum", "remain"]
    
    valExtData = [i for i in data if i[columns.index(ext)] < val_ext]
        
    answer = sorted(valExtData, key=lambda x : x[columns.index(sort_by)])
        
    return answer