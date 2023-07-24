n = list(map(int, input().split()))
lis = list(map(int, input().split()))
lis.sort()

result = 0
count = 0

for i in lis:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)
