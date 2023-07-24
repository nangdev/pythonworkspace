n = int(input())
for i in range(n):
    s = int(input())
    result = 1
    for j in range(2, s+1):
        if j % 2 == 0:
            result -= j
        else:
            result += j
    print(f"#{i+1} {result}")
