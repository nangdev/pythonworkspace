t = int(input())
for i in range(t):
    dinum = int(input())
    result = 0
    a = 0
    for _ in range(dinum):
        commend = list(map(int, input().split()))
        if commend[0] == 0:
            result += a
        elif commend[0] == 1:
            a += commend[1]
            result += a
        else:
            a += -commend[1]
            if a < 0:
                a = 0
                continue
            result += a
    print(f"#{i+1} {result}")
