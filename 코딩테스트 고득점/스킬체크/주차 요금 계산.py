import math

def solution(fees, records):
    data = [[] for _ in range(10000)]
    allTime = 23* 60 + 59
    answer = []

    for r in records:
        Time, Id, InOut = r.split(" ")
        h, m = map(int, Time.split(":"))
        data[int(Id)].append([h * 60 + m, InOut])

    for d in data:
        if d:
            if len(d) % 2 != 0:
                d.append([23*60 + 59])
            money = 0
            totalTime = 0
            for i in range(len(d)):
                if i%2 == 0:
                    totalTime -= d[i][0]
                else:
                    totalTime += d[i][0]

            if totalTime <= fees[0]:
                money = fees[1]
            else:
                money = fees[1] + math.ceil((totalTime-fees[0]) / fees[2]) * fees[3]

            answer.append(money)

    return answer