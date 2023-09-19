for l in range(1, 11):
    t = input()
    mag = []
    for _ in range(100):
        mag.append(list(input().split()))

    check = ""
    result = 0

    for i in range(100):
        for j in range(100):
            if mag[j][i] != '0':
                check += mag[j][i]
        result += check.count("12")
        check = ""

    print(f"#{l} {result}")
