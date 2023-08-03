import copy
t = int(input())
for i in range(t):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(input().split()))
    rotae = [['0']*n for i in range(n)]
    result = [[] for i in range(n)]
    for _ in range(3):
        for j in range(n):
            for k in range(n):
                rotae[k][n-j-1] = matrix[j][k]
        for y in range(n):
            result[y].append("".join(rotae[y]))
        matrix = copy.deepcopy(rotae)
    print(f"#{i+1}")
    for rmaks in result:
        print(*rmaks)
