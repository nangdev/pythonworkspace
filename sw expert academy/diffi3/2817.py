def dfs(n, sum):
    global ans

    if sum > K:
        return

    if n == N:
        if sum == K:
            ans += 1
        return

    dfs(n+1, sum+arr[n])
    dfs(n+1, sum)


t = int(input())
for i in range(1, t+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = 0
    dfs(0, 0)

    print(f"#{i} {ans}")
