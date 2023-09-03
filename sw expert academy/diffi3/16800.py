import math
t = int(input())
for i in range(1, t+1):
    m = int(input())
    j = 1
    count = 0
    for l in range(int((math.sqrt(m))), 1, -1):
        if m % l == 0:
            j = l
            count += l-1
            break
    k = m//j
    if m // j == m:
        print(f"#{i} {m-1}")
        continue
    count += k-1
    print(f"#{i} {count}")
