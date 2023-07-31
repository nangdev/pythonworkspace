n = int(input())
for i in range(n):
    cash = int(input())
    cashlis = [0, 0, 0, 0, 0, 0, 0, 0]
    while cash != 0:
        cashlis[0] = cash // 50000
        cash %= 50000
        cashlis[1] = cash // 10000
        cash %= 10000
        cashlis[2] = cash // 5000
        cash %= 5000
        cashlis[3] = cash // 1000
        cash %= 1000
        cashlis[4] = cash // 500
        cash %= 500
        cashlis[5] = cash // 100
        cash %= 100
        cashlis[6] = cash // 50
        cash %= 50
        cashlis[7] = cash // 10
        cash %= 10
    print(f"#{i+1}")
    for i in cashlis:
        print(i, end=" ")
    print()
