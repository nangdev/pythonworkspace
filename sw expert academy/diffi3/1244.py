t = int(input())
for i in range(1, t+1):
    num, n = input().split()
    numlis = []
    for j in num:
        numlis.append(int(j))

    numa, numb, indexa, indexb = 0, 0, 0, 0
    for _ in range(int(n)):
        numa = max(numlis)
        numb = min(numlis)
        indexa = max(numlis).index()
        indexb = min(numlis).index()
