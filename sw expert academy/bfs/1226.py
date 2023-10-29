def bfs(si, sj):
    q = []
    v = [[0]*16 for _ in range(16)]

    q.append([si, sj])
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if arr[ci][cj] == 3:
            return 1

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < 16 and 0 <= nj < 16 and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append([ni, nj])
                v[ni][nj] = 1

    return 0


def dfs(si, sj):
    global ans
    ci, cj = si, sj

    if arr[ci][cj] == 3:
        ans = 1
        return

    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        ni, nj = ci+di, cj+dj
        if 0 <= ni < 16 and 0 <= nj < 16 and v[ni][nj] == 0 and arr[ni][nj] != 1:
            v[ni][nj] = 1
            dfs(ni, nj)


for i in range(1, 11):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    v = [[0]*16 for _ in range(16)]
    si, sj = 1, 1
    dfs(si, sj)
    print(f"#{n} {ans}")
