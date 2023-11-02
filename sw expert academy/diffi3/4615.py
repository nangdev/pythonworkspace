t = int(input())
for i in range(1, t+1):
    N, play = map(int, input().split())
    osalo = [[0]*N for _ in range(N)]
    if N == 4:
        osalo[1][1], osalo[2][2] = 2, 2
        osalo[1][2], osalo[2][1] = 1, 1
    elif N == 6:
        osalo[2][2], osalo[3][3] = 2, 2
        osalo[2][3], osalo[3][2] = 1, 1
    else:
        osalo[3][3], osalo[4][4] = 2, 2
        osalo[3][4], osalo[4][3] = 1, 1
    for _ in range(play):
        comm = list(map(int, input().split()))

        osign = False
        ksign = False

        re_x, re_y = 0, 0

        if comm[2] == 1:
            for dx, dy in [1, 0], [-1, 0], [0, -1], [0, 1]:
                try:
                    if osalo[comm[1]-1+dx][comm[0]-1+dy] == 2:
                        osign = True
                        re_x = comm[1]-1+dx
                        re_y = comm[0]-1+dy
                except:
                    continue

            if osign:
                for dx, dy in [-2, 0], [-2, 2], [0, 2], [2, 2], [2, 0], [2, -2], [0, -2], [-2, -2]:
                    try:
                        if osalo[comm[1]-1+dx][comm[0]-1+dy] == 1:
                            ksign = True
                    except:
                        continue

                if ksign:
                    osalo[comm[1]-1][comm[0]-1] = 1
                    osalo[re_x][re_y] = 1
                else:
                    continue

            else:
                continue

        else:
            for dx, dy in [1, 0], [-1, 0], [0, -1], [0, 1]:
                try:
                    if osalo[comm[1]-1+dx][comm[0]-1+dy] == 1:
                        osign = True
                        re_x = comm[1]-1+dx
                        re_y = comm[0]-1+dy
                except:
                    continue

            if osign:
                for dx, dy in [-2, 0], [-2, 2], [0, 2], [2, 2], [2, 0], [2, -2], [0, -2], [-2, -2]:
                    try:
                        if osalo[comm[1]-1+dx][comm[0]-1+dy] == 2:
                            ksign = True
                    except:
                        continue

                if ksign:
                    osalo[comm[1]-1][comm[0]-1] = 2
                    osalo[re_x][re_y] = 2
                else:
                    continue

            else:
                continue

    black, white = 0, 0
    for ans in osalo:
        black += ans.count(1)
        white += ans.count(2)

    print(f"#{i} {black} {white}")
