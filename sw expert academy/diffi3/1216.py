for _ in range(1, 11):
    t = input()
    pail = []
    for _ in range(100):
        pail.append(list(input()))

    result = 1

    for i in range(100):
        for j in range(100):
            for k in range(j+1, 100):
                if pail[i][j:k] == pail[i][k-1:j-1:-1]:
                    result = max(result, len(pail[i][j:k]))

    rotate = list(map(list, zip(*pail)))
    for i in range(100):
        for j in range(100):
            for k in range(j+1, 100):
                if rotate[i][j:k] == rotate[i][k-1:j-1:-1]:
                    result = max(result, len(rotate[i][j:k]))

    print(f"#{t} {result}")
