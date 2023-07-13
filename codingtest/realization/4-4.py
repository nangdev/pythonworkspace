ran = list(map(int, input().split()))
a, b, c = map(int, input().split())
gps = [a, b]
maping = []
result = 0
direc = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 북동남서
for i in range(ran[0]):
    maping.append(list(map(int, input().split())))

while True:
    pre_dir = c
    count = 0
    # 1번째 조건
    for _ in range(4):
        pre_gps = gps
        pre_dir -= 1
        next_x = pre_gps[0] + direc[pre_dir][0]
        next_y = pre_gps[1] + direc[pre_dir][1]
        if 0 <= next_x < ran[0] and 0 <= next_y < ran[1] and maping[next_x][next_y] == 0:
            c = pre_dir
            gps = [next_x, next_y]
            result += 1
            count += 1
            break
    if count == 1:
        continue

    # 2번째 조건
    if c == 0:
        b += 1
    elif c == 1:
        a -= 1
    elif c == 2:
        b -= 1
    else:
        a += 1

    if a == ran[0] or a < 0 or b == ran[1] or b < 0:
        break
print(result)
