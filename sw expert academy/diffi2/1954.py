t = int(input())
for i in range(t):
    n = int(input())
    snail = [[0]*n for i in range(n)]
    cop = n
    c = 1
    x, y = 0, 0
    while c <= cop:
        snail[x][y] = c
        y += 1
        c += 1
        if y == n:
            y -= 1
            for j in range(n-1):
                x += 1
                snail[x][y] = c
                c += 1
        if x == n:
            pass
