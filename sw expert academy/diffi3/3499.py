t = int(input())
for i in range(1, t+1):
    N = int(input())
    arr = input().split()

    ans = []

    if N % 2 == 0:
        a = arr[:N//2]
        b = arr[N//2:]
        for k in range(N//2):
            ans.append(a[k])
            ans.append(b[k])
        print(f"#{i} ", end="")
        print(*ans)

    else:
        a = arr[:N//2+1]
        b = arr[N//2+1:]
        for k in range(N//2):
            ans.append(a[k])
            ans.append(b[k])
        ans.append(a[-1])
        print(f"#{i} ", end="")
        print(*ans)
