n = int(input())
lis = list(input().split())
result = [1, 1]
for i in lis:
    if i == 'L':
        result[1] -= 1
        if result[1] == 0:
            result[1] += 1
            continue
    elif i == 'R':
        result[1] += 1
        if result[1] > n:
            result[1] -= 1
            continue
    elif i == 'U':
        result[0] -= 1
        if result[0] == 0:
            result[0] += 1
            continue
    else:
        result[0] += 1
        if result[0] > n:
            result[0] -= 1
            continue
print(f"{result[0]} {result[1]}")
