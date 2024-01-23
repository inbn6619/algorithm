def minus(t1, t2):
    t1 = list(map(int, t1.split(":")))
    t1 = t1[0] * 60 + t1[1]
    t2 = list(map(int, t2.split(":")))
    t2 = t2[0] * 60 + t2[1]   
    
    return t2 - t1

def changeString(s):
    return s.replace("C#", 'c').replace("C#", 'c').replace("D#", 'd').replace("F#", 'f').replace("G#", 'g').replace("A#", 'a')

def solution(m, musicinfos):
    
    result = []

    m = changeString(m)
    
    for music in musicinfos:
        s, e, n, char = music.split(",")
        
        char = changeString(char)
        
        time = minus(s, e)
        
        l = len(char)
        k = 1
        
        while time > l * k:
            k += 1
        
        char *= k
        char = char[:time]        
                
        if m in char:
            result.append([n, time])

    if result:
        sortedResult = sorted(result, key=lambda x: x[1], reverse=True)
        
        answer = sortedResult[0][0]
    else:
        return "(None)"
        
    
    return answer