t = int(input())
for i in range(1, t+1):
    N = int(input())
    arr = []
    stop = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    P = int(input())
    for _ in range(P):
        stop.append(int(input()))

    ans = []

    for k in stop:
        poss = 0
        for a, b in arr:
            if a <= k <= b:
                poss += 1
        ans.append(poss)

    print(f"#{i} ", end="")
    print(*ans)
