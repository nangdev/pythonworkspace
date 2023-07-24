n = int(input())
for i in range(n):
    case_num = int(input())
    lis = list(map(int, input().split()))
    result = 0

    for j in range(case_num):
        result += max(lis)-lis[0]
        del lis[0]

    print(f"#{i+1} {result}")
