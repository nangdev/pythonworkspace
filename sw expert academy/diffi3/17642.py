t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if b-a == 1 or b == a:
        print(f"#{i+1} -1")
        continue
    result = 0
    prob = b-a
    if prob == 3:
        print(f"#{i+1} 1")
        continue
    if prob % 2 == 0:
        while prob != 1:
            prob //= 2
            result += 1
    else:
        prob -= 3
        result += 1
        while prob != 1:
            prob //= 2
            result += 1
    print(f"#{i+1} {result}")
