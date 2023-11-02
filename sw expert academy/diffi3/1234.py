for i in range(1, 11):
    n, ques = input().split()
    arr = list(ques)
    num = int(n)

    k = 0
    while k != num-1:
        if arr[k] == arr[k+1]:
            arr.pop(k)
            arr.pop(k)
            k = 0
            num -= 2
        else:
            k += 1

    ans = "".join(arr)
    print(f"#{i} {ans}")
