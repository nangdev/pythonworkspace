t = int(input())
for i in range(1, t+1):
    n = int(input())
    farm = []
    for _ in range(n):
        farm.append(list(map(int, input())))
    result = 0
    bun = 0
    for j in range(n):
        if j < n//2:
            result += sum(farm[j][n//2-j:n//2+j+1])
        elif j == n//2:
            result += sum(farm[j])
        else:
            bun += 2
            result += sum(farm[j][n//2-(j-bun):n//2+(j-bun+1)])
    print(f"#{i} {result}")
