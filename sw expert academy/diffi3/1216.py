for _ in range(1, 11):
    t = input()
    pail = []
    for _ in range(100):
        pail.append(list(input()))

    result = 0

    for i in range(100):
        for j in range(100):
            for k in range(j+1, 100):
                if pail[i][j:k] == pail[i][k:j:-1]:
                    pass
