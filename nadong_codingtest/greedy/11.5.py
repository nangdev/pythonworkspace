from itertools import combinations

n = list(map(int, input().split()))
lis = list(map(int, input().split()))

result = list(combinations(lis, 2))
for i in result:
    if i[0] == i[1]:
        result.remove(i)

print(len(result))
