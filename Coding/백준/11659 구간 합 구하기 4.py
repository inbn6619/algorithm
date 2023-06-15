# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
import sys

input = sys.stdin.readline


N, M = map(int, input().split()) # 수의 개수, 합을 구해야하는 횟수

num_list = list(map(int, input().split()))

num = 0

slist = [0]

for n in num_list:
    slist.append(num + n)
    num += n

for m in range(M):
    i, j = map(int, input().split()) # 인덱스 각자 -1 해줘야됨

    print(slist[j] - slist[i-1])