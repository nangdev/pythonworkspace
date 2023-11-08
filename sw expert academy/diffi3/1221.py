num = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
       "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

for i in range(int(input())):
    cond = input().split()
    prob = input().split()

    ans = sorted(prob, key=lambda x: num[x])

    print(cond[0])
    print(*ans)
