n = int(input())
for i in range(n):
    numlen = input()
    numlis = list(map(int, input().split()))
    numlis.sort()
    print(f"#{i+1}", end=" ")
    for j in numlis:
        print(j, end=" ")
    print()
