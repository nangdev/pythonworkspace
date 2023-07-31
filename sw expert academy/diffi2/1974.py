n = int(input())
for i in range(n):
    sdouk = []
    break_count = 0
    for _ in range(9):
        sdouk.append(list(map(int, input().split())))
    for j in sdouk:  # 가로
        if sum(j) != 45:
            print(f"#{i+1} 0")
            break_count += 1
            break
    if break_count == 1:
        continue
    for x in range(9):  # 세로
        count = 0
        for y in range(9):
            count += sdouk[y][x]
        if count != 45:
            print(f"#{i+1} 0")
            break_count += 1
            break
    if break_count == 1:
        continue
    for x in range(0, 9, 3):  # 9*9
        for y in range(0, 9, 3):
            count = 0
            for k in range(3):
                count += sum(sdouk[k+x][y:y+3])
            if count != 45:
                print(f"#{i+1} 0")
                break_count += 1
                break
    if break_count == 1:
        continue
    print(f"#{i+1} 1")
