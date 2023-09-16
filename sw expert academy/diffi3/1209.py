for _ in range(10):
    t = int(input())
    lis = []
    for _ in range(100):
        lis.append(list(map(int, input().split())))
    result = []
    for i in lis:
        result.append(sum(i))
    for i in range(100):
        coun = 0
        for j in range(100):
            coun += lis[j][i]
        result.append(coun)
    count_cros = 0
    count_revcros = 0
    for i in range(100):
        count_cros += lis[i][i]
        count_revcros += lis[i][99-i]
    result.append(count_cros)
    result.append(count_revcros)
    res = max(result)
    print(f"#{t} {res}")
