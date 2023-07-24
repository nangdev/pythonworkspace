n = list(input())
result = []
num = 0
for i in n:
    if i.isdigit():
        num += int(i)
        continue
    result.append(i)
result.sort()
print("".join(result) + str(num))
