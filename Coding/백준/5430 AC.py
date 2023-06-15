from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    func = input().rstrip()
    N = int(input())
    lst = deque(input().rstrip()[1:-1].split(','))
    back = 0
    check = 0

    if N == 0:
        lst = []

    for i in func:
        if i == 'R':
            back += 1
        elif i == 'D':
            if len(lst) < 1:
                check = 1
                print('error')
                break
            else:
                if back % 2 == 0:
                    lst.popleft()
                else:
                    lst.pop()

    if check == 0:
        if back % 2 != 0:
            lst.reverse()
            print('[' + ','.join(lst) + ']')
        else:
            print('[' + ','.join(lst) + ']')
