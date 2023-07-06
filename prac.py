from itertools import combinations

lis = [1, 3, 4, 5, 6]

for i in range(1, 6):
    comb = list(combinations(lis, i))
    for j in comb:
        lis.append(sum(j))

print(lis)
