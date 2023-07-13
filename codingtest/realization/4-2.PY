import time
n = int(input())
start = time.time()
timer = [0, 0, 0, 0, 0]
result = 0
for _ in range(n*3600 + 3540 + 59):
    timer[4] += 1
    if timer[4] == 10:
        timer[3] += 1
        timer[4] = 0
    if timer[3] == 6:
        timer[2] += 1
        timer[3] = 0
    if timer[2] == 10:
        timer[1] += 1
        timer[2] = 0
    if timer[1] == 6:
        timer[0] += 1
        timer[1] = 0
    if 3 in timer:
        result += 1
end = time.time()
print(result)
print(f"{end-start: 5f} sec")
