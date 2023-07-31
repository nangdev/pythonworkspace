n = int(input())
for i in range(n):
    clo = list(map(int, input().split()))
    hour = clo[0] + clo[2]
    minuite = clo[1] + clo[3]
    if hour > 12:
        hour -= 12
    if minuite >= 60:
        minuite -= 60
        hour += 1
    print(f"#{i+1} {hour} {minuite}")
