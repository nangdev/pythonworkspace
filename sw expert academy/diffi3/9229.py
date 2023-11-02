def dfs(n, num, weight):
    global ans

    if weight > maxwei:
        return

    if n == number:
        if num == 2:
            ans = max(ans, weight)
            return
        return

    dfs(n+1, num+1, weight+arr[n])
    dfs(n+1, num, weight)


t = int(input())
for i in range(1, t+1):
    number, maxwei = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    dfs(0, 0, 0)

    if ans == 0:
        ans = -1

    print(f"#{i} {ans}")
