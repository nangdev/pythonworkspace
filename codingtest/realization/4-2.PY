n = int(input())
time = [n, 0, 0, 0, 0]
result = 0
for _ in range(n*3600 + 3540 + 59):
    time[4] += 1
    if time[4] == 10:
        time[3] += 1
        time[4] = 0
    if time[3] == 6:
        time[2] += 1
        time[3] = 0
    if time[2] == 10:
        time[1] += 1
        time[2] = 0
    if time[1] == 6:
        time[0] += 1
        time[1] = 0
    if 3 in time:
        result += 1
print(result)
