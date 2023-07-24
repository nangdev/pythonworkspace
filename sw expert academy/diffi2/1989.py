n = int(input())
for i in range(n):
    pail = input()
    count = 0
    for j in range(len(pail)//2):
        if pail[j] != pail[-(j+1)]:
            print(f"#{i+1} 0")
            count += 1
            break
    if count == 0:
        print(f"#{i+1} 1")
