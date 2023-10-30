for i in range(1, 11):
    n = int(input())
    cod = list(map(int, input().split()))
    dirnum = int(input())
    arr = input().split()

    j = 0
    while dirnum != 0:
        if arr[j] == 'I':
            for k in range(int(arr[j+2])):
                cod.insert(int(arr[j+1])+k, int(arr[j+3+k]))
            j += int(arr[j+2]) + 3
            dirnum -= 1
        elif arr[j] == 'D':
            for _ in range(int(arr[j+2])):
                cod.pop(int(arr[j+1])+1)
            j += 3
            dirnum -= 1
        elif arr[j] == 'A':
            for k in range(int(arr[j+1])):
                cod.append(int(arr[j+2])+k)
            j += int(arr[j+1]) + 2
            dirnum -= 1

    print(f"#{i} ", end="")
    print(*cod[:10])
