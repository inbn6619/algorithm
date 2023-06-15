# -, + 추출 하기
# - 기준 괄호

arr = input().split('-')


for i in range(len(arr)):
    plus = arr[i].split('+')
    num = 0
    for p in plus:
        num += int(p)

    arr[i] = num

result = arr[0]

for t in range(1, len(arr)):
    result -= arr[t]

print(result)