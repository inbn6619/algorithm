import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = list()

for n in range(N):
    x = int(input())

    if x == 0:
        if heap:
            print(heapq.heappop())