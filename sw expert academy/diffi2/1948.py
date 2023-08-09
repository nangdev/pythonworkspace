t = int(input())
for i in range(t):
    day = list(map(int, input().split()))
    daylis = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0
    for j in range(day[0], day[2]):
        result += daylis[j]
    result += day[3]-day[1]+1
    print(f"#{i+1} {result}")
