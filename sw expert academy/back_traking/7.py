def dfs(n, sm):
    global ans
    if ans <= sm:
        return

    if n == N-1:
        # 아 이렇게 하면 어차피 v가 다 0이라 처음게 나오는구나
        ans = min(ans, sm+distric[N][1])
        return

    for j in range(1, N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, sm+distric[n][j])
            v[j] = 0


t = int(input())
for i in range(1, t+1):
    N = int(input())
    distric = []
    for _ in range(N):
        distric.append(list(map(int, input().split())))
    v = [1]+[0]*N
    ans = 100*N**2
    dfs(0, 0)
    print(f"#{i} {ans}")
