from itertools import combinations

n = int(input())
lis = list(map(int, input().split()))

for _ in range(2, n+1):
    comb = list(combinations(lis, n))
    for i in comb:
        lis.append(sum(i))

print(lis)
