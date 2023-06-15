N, K = map(int, input().split())

array = [int(i) for i in input().split()]

array.sort()

print(array[K-1])
