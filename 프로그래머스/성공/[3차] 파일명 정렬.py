def solution(files):    
    result = list()
    
    for file in files:

        for c in range(len(file)):
            if file[c].isdigit():
                h = file[:c]
                target = file[c:]
                break
                
        n = ""
        t = ""
                
        for tar in range(len(target)):
            if not target[tar].isdigit():
                n = target[:tar]
                t = target[tar:]
                break
        
        if n == "":
            n = target                

        result.append([h, n, t])
        
    sortedResult = sorted(result, key=lambda x : (x[0].lower(), int(x[1])))

    answer = [''.join(i) for i in sortedResult]

    return answer