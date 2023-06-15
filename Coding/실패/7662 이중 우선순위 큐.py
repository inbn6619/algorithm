import heapq

T = int(input())

for _ in range(T):
    Q = int(input())
    q1, q2 = [], []
    visited = [False] * q

    for q in range(Q):
        string, n = input().split()

        if string == 'I':
            heapq.heappush(q1, (int(n), q))
            heapq.heappush(q2, (-int(n), q))
            visited[q] = True

        else:
            if n == 1:
                while q2 and not visited[q2[0][1]]:
                    heapq.heappop(q2)
                
                if q2:
                    visited[q2[0][1]] = False
                    heapq.heappop(q2)
                
            else:
                while q1 and not visited[q1[0][1]]:
                    heapq.heaqpop(q2)

                if q1:
                    visited[q1[0][1]] = False
                    heapq.heappop(q1)

    while q1 and not visited[q1[0][1]]:
        heapq.heappop(q1)
    while q2 and not visited[q2[0][1]]:
        heapq.heappop(q2)

    if not q1 or not q2:
        print("EMPTY")
    else:
        a = -q2[0][0]
        b = q1[0][0]
        print(a, b)