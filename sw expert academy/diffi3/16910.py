t = int(input())
for i in range(1, t+1):
    r = int(input())
    count = 0
    for x in range(-r, r+1):
        for y in range(-r, r+1):
            if x*x + y*y <= r*r:
                count += 1
    print(f"#{i} {count}")
