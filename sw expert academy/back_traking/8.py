def dfs(n, num, ci, cj):
    if n == 7:
        sset.add(num)
        return

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci+di, cj+dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(n+1, num*10+arr[ni][nj], ni, nj)


t = int(input())
for i in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    print(arr)

    # 가능한 모든 위치 순회(si,sj) 기준으로 백트래킹
    sset = set()
    for si in range(4):
        for sj in range(4):
            dfs(1, arr[si][sj], si, sj)

    print(f"#{i} {len(sset)}")
