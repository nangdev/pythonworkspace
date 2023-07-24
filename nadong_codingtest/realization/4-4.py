n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵
d = [[0]*m for _ in range(n)]
x, y, direc = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문처리

mapping = []
for i in range(n):
    mapping.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direc
    direc -= 1
    if direc == -1:
        direc = 3


count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direc]
    ny = y + dy[direc]
    # 안가본대라면
    if d[nx][ny] == 0 and mapping[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    # 갈 곳이 없다면
    if turn_time == 4:
        nx = x - dx[direc]
        ny = y - dy[direc]
        # 갔던곳이 있다
        if mapping[nx][ny] == 0:
            x = nx
            y = ny
        # 바다다
        else:
            break
        turn_time = 0
print(count)
