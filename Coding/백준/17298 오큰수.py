t = int(input())

numbers = list(map(int, input().split()))

# t = 4

# numbers = [3, 5, 2, 7]

answer = [0 for _ in range(t)]

stack = [0]

for i in range(1, t):
    while stack and numbers[stack[-1]] < numbers[i]:
        prev = stack[-1]
        answer[prev] = numbers[i]
        stack.pop()
    stack.append(i)

for num in stack:
    answer[num] = -1

print(' '.join([str(i) for i in answer]))