t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    pro = []
    dic = {"0001101": 0, "0011001": 1, "0010011": 2, "0111101": 3, "0100011": 4,
           "0110001": 5, "0101111": 6, "0111011": 7, "0110111": 8, "0001011": 9}
    for _ in range(n):
        pro.append(input())
    passline = 0
    code = []
    for j in range(n):
        if pro[j].count('0') != m:
            passline = j
            break

    for k in range(m-1, 0, -1):
        if pro[passline][k] == '1':
            for p in range(8):
                code.append(dic[pro[passline][(k-7)-(p*7)+1:k-(p*7)+1]])
            break

    result = 0
    for l in range(8):
        if l % 2 == 0:
            result += code[l]*3
        else:
            result += code[l]
    if result % 10 == 0:
        print(f"#{i} {sum(code)}")
    else:
        print(f"#{i} 0")
