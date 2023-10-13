def dfs(num, sum, cnt):
    global result

    # 가지치기
    if sum > k:
        return

    # 종료 조건
    if num == N:
        if sum == k and cnt == n:
            result += 1
        return

    # 사용하는 경우
    dfs(num+1, sum+lst[num], cnt+1)
    # 사용하지 않는 경우
    dfs(num+1, sum, cnt)


t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    lst = [l for l in range(1, 13)]
    N = 12
    result = 0

    dfs(0, 0, 0)
    print(f"#{i} {result}")
