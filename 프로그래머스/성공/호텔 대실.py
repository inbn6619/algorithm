from collections import deque

def solution(book_time):
    
    def changeTime(string):
        h, m = map(int, string.split(":"))

        return h * 60 + m
    
    for i in range(len(book_time)):
        s, e = book_time[i]
        s = changeTime(s)
        e = changeTime(e) + 10
        book_time[i][0] = s
        book_time[i][1] = e
    
    # print(book_time)
    
    sortedBookTime = sorted(book_time, key=lambda x : x[0])
    
    # print(sortedBookTime)
    
    deq = deque(sortedBookTime)
    
    room = [deq.popleft()]
    
    while deq:
        check = False
        
        for i in range(len(deq)):
            s, e = deq[i]
            if room[-1][-1] <= s:
                room[-1].extend([s, e])
                del deq[i]
                check = True
                break
        if not check:
            room.append(deq.popleft())
    
    # print(room)
        
    return len(room)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]	))