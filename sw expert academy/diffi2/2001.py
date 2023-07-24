case_num = int(input())
for j in range(case_num):
    n, m = map(int, input().split())
    pari = []
    for i in range(n):
        pari.append(list(map(int, input().split())))
    offset = n-m+1
    result = 0
    for x in range(offset):
        for y in range(offset):
            summ = 0
            for k in range(m):
                summ += sum(pari[x+k][y:y+m])
            result = max(result, summ)
    print(f"#{j+1} {result}")
