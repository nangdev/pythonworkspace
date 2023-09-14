for i in range(1, 11):
    dump = int(input())
    lis = list(map(int, input().split()))
    indexa, indexb = 0, 0
    for _ in range(dump):
        indexa = lis.index(max(lis))
        indexb = lis.index(min(lis))
        lis[indexa] -= 1
        lis[indexb] += 1
    result = max(lis) - min(lis)
    print(f"#{i} {result}")
