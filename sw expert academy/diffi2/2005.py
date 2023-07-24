n = int(input())
for i in range(n):
    s = int(input())
    print(f"#{i+1}")
    lis = [0, 1, 0]
    for j in range(s):
        lis2 = []
        if j == 0:
            print(1)
            continue
        for k in range(len(lis)+1):
            if k == 0:
                lis2.append(0)
            elif k == len(lis):
                lis2.append(0)
            else:
                lis2.append(lis[k]+lis[k-1])
        for x in lis2:
            if x == 0:
                continue
            print(x, end=" ")
        print()
        lis = lis2
