import sys
import heapq

input = sys.stdin.readline

X = int(input())

heap = list()

for _ in range(X):
    x = int(input())

    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-x, x))
    
