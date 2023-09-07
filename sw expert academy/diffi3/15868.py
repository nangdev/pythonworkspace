t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    xor = []
    for _ in range(n):
        xor.append(list(map(int, input())))
    c = 0
    for j in range(m):
        if xor[0][j] == xor[1][j]:
            print(f"#{i} no")
            c += 1
            break
    if c == 1:
        continue
    print(f"#{i} yes")
