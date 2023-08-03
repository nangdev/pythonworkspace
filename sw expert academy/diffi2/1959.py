t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    nlis = list(map(int, input().split()))
    mlis = list(map(int, input().split()))
    result = []
    ran = min(n, m)
    for j in range(abs(n-m)+1):
        count = 0
        for k in range(ran):
            if n > m:
                count += nlis[k+j]*mlis[k]
            else:
                count += nlis[k]*mlis[k+j]
        result.append(count)
    print(f"#{i+1} {max(result)}")
