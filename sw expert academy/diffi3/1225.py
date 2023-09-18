for _ in range(10):
    t = int(input())
    password = list(map(int, input().split()))
    num = 0
    while 1:
        temp = 0
        num += 1
        if num == 6:
            num = 1
        password[0] -= num
        if password[0] <= 0:
            del password[0]
            break
        temp = password[0]
        del password[0]
        password.append(temp)

    password.append(0)
    print(f"#{t}", end=" ")
    print(*password)
