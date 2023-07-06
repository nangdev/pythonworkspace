n = list(map(int, input().split()))
lis = list(map(int, input().split()))
res = 0
ma1 = max(lis)
lis.remove(ma1)
ma2 = max(lis)
for i in range(1, n[1]+1):
    if i % n[2] == 0:
        res += ma2
        continue
    res += ma1

print(res)
