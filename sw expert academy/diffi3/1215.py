for l in range(1, 11):
    n = int(input())
    pail = []
    for _ in range(8):
        pail.append(list(input()))
    result = 0

    # 가로
    for i in pail:
        for j in range(9-n):
            if i[j:j+n] == i[j+n:j:-1]:
                result += 1

    # 세로
    for i in range(8):
        for j in range(9-n):
            ch = ""
            for k in range(n):
                ch += pail[j+k][i]
            if ch == ch[::-1]:
                result += 1

    print(f"#{l} {result}")
