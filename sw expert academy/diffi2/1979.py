n = int(input())
for i in range(n):
    m, k = map(int, input().split())
    mapping = []
    for l in range(m):
        mapping.append(list(map(int, input().split())))
        mapping[l].append(0)
    mapping.append([0 for i in range(m+1)])
    print(mapping)
    result = 0
    for x in range(m):
        count = 0
        for y in range(m):
            count = 0
            if count == k:
                if mapping[x][y+1] == 0:
                    result += 1
                    count = 0
                else:
                    count = 0

    for x in range(m):
        count = 0
        for y in range(m):
            count += mapping[y][x]
            if count == k:
                if mapping[y+1][x] == 0:
                    result += 1
                    count = 0
                else:
                    count = 0
    print(f"#{i+1} {result}")
