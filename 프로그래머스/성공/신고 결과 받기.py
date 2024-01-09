def solution(id_list, report, k):
    
    d = dict()
    t = dict()
    
    for i in id_list:
        d[i] = set()
        t[i] = 0
            
    for r in report:
        i, r = r.split()
        
        d[r].add(i)
            
    for key,value in d.items():
        if len(value) >= k:
            for v in value:
                t[v] += 1
                
    
    answer = list(t.values())
    
    return answer