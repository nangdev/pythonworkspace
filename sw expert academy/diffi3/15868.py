t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    xor = []
    for _ in range(n):
        xor.append(list(map(int, input())))
