def dfs(n, taste, cal):
    global ans
    if cal > L:
        return

    if n == N:
        ans = max(ans, taste)
        return

    dfs(n+1, taste + arr[n][0], cal + arr[n][1])
    dfs(n+1, taste, cal)


t = int(input())
for i in range(1, t+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    v = [0] * N
    dfs(0, 0, 0)
    print(f"#{i} {ans}")
