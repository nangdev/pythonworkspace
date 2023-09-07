t = int(input())
for i in range(1, t+1):
    a, b = input().split()
    if len(a) % 2 == 0:
        newa = (a*60)[:60]
        newb = (b*60)[:60]
    else:
        newa = (a*67)[:67]
        newb = (b*67)[:67]
    if newa == newb:
        print(f"#{i} yes")
    else:
        print(f"#{i} no")
