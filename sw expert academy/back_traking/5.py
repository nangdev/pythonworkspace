def dfs(n, sm):
    global ans
    if ans <= sm:
        return

    if n > 12:
        ans = min(ans, sm)
        return

    dfs(n+1, sm+day*using[n])  # 일일권
    dfs(n+1, sm+mon)  # 한달권
    dfs(n+3, sm+mon3)  # 분기권
    dfs(n+12, sm+year)  # 일년권


t = int(input())
for i in range(1, t+1):
    day, mon, mon3, year = map(int, (input().split()))
    using = [0] + list(map(int, (input().split())))

    # 백트래킹
    ans = 3000*12
    dfs(0, 0)

    # 그리디
    D = [0]*13
    for k in range(1, 13):
        # 가능한 4가지 방법중 i달의 최소비용
        mn = D[k-1] + using[k]*day
        mn = min(mn, D[k-i]+mon)
        if k >= 3:
            mn = min(mn, D[i-3]+mon3)
        if k >= 12:
            mn = min(mn, D[i-12]+year)

    print(f"#{i} {ans}")
