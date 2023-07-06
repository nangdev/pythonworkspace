lis = list(input())

data = []
for i in lis:
    data.append(int(i))

result = data[0]
for i in range(len(data)-1):
    # if i == 0 and data[i] != 0:
    #     result = data[i]

    if data[i] == 0 or data[i] == 1:
        result += data[i+1]
        continue
    result *= data[i+1]

print(result)
