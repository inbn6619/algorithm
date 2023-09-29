import math

def find_divisors(n):
    divisors = []
    sqrt_n = int(math.sqrt(n))
    
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            divisors.append(i)
            # 제곱근을 기준으로 한 쌍의 약수를 찾음
            if i != n // i:
                divisors.append(n // i)
    
    return divisors

# 숫자를 입력받고 약수를 찾습니다.
number = int(input("약수를 찾을 숫자를 입력하세요: "))
result = find_divisors(number)

print(f"{number}의 약수는 {result}입니다.")