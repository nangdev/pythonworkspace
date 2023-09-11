for i in range(1, 11):
    n = int(input())
    bullis = list(map(int, input().split()))
    count = 0
    for b in range(2, n-1):
        if bullis[b] <= bullis[b-1] or bullis[b] <= bullis[b+1]:
            continue
        elif bullis[b] <= bullis[b-2] or bullis[b] <= bullis[b+2]:
            continue
        else:
            count += bullis[b]-max(bullis[b-1], bullis[b-2],
                                   bullis[b+1], bullis[b+2])
    print(f"#{i} {count}")
