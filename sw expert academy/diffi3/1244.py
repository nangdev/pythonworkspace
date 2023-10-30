def dfs(n):
    global ans
    if n == cnt:
        ans = max(ans, int("".join(map(str, arr))))
        return

    for i in range(N-1):
        for j in range(i+1, N):
            arr[i], arr[j] = arr[j], arr[i]
            chk = int("".join(map(str, arr)))
            if (n, chk) not in v:
                dfs(n+1)
                v.append((n, chk))
            arr[i], arr[j] = arr[j], arr[i]


t = int(input())
for i in range(1, t+1):
    lis, cnt = input().split()
    N = len(lis)
    v = []
    arr = list(map(int, lis))
    cnt = int(cnt)
    ans = 0
    dfs(0)
    print(f"{i} {ans}")
