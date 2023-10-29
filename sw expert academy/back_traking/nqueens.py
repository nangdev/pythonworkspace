def dfs(n):
    global ans

    if n == N:
        ans += 1
        return

    for j in range(N):
        if v1[j] == 0 and v2[n+j] == 0 and v3[n-j] == 0:
            v1[j] = 1
            v2[n+j] = 1
            v3[n-j] = 1
            dfs(n+1)
            v1[j] = 0
            v2[n+j] = 0
            v3[n-j] = 0


t = int(input())
for i in range(1, t+1):
    N = int(input())
    v1 = [0]*N
    v2 = [0]*(N*2-1)  # right up
    v3 = [0]*(N*2-1)  # left up
    diag = [[0]*N for _ in range(N)]
    ans = 0
    dfs(0)
    print(f"#{i} {ans}")
