def hanoi(n, start, end, auxiliary1, auxiliary2, auxiliary3):
    if n == 1:
        print(f"Move disk 1 from {start} to {end}")
        return
    hanoi(n - 2, start, auxiliary1, auxiliary2, auxiliary3, end)
    print(f"Move disk {n - 1} from {start} to {auxiliary3}")
    print(f"Move disk {n} from {start} to {end}")
    print(f"Move disk {n - 1} from {auxiliary3} to {end}")
    hanoi(n - 2, auxiliary1, end, start, auxiliary2, auxiliary3)

# 예시: 3개의 원반을 5개의 기둥으로 옮기기
hanoi(5, 'A', 'B', 'C', 'D', 'E')
