def bfs(si, sj):
    q = []
    v = [[0]*N for _ in range(N)]

    q.append([si, sj])
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if arr[ci][cj] == 3:
            return v[ci][cj] - 2

        # 4방향 범위내이고, 1이 아니고, 미방문이면
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append([ni, nj])
                v[ni][nj] = v[ci][cj] + 1

    # 목적지에 도달하지 못한 경우
    return 0


t = int(input())
for i in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    si, sj = 0, 0

    for a in range(N):
        for b in range(N):
            if arr[a][b] == 2:
                si, sj = a, b
                break

    ans = bfs(si, sj)
    print(f"#{i} {ans}")
