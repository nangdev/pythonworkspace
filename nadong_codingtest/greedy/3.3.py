n = list(map(int, input().split()))
lis = []
for _ in range(n[0]):
    lis.append(list(map(int, input().split())))
result = 0
for i in lis:
    if min(i) > result:
        result = min(i)
print(result)


# 해설 보고나서

n = list(map(int, input().split()))
lis = []
result = 0
for _ in range(n[0]):
    lis.append(list(map(int, input().split())))
    if min(lis) > result:
        result = min(lis)
print(result)
