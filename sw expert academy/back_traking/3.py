def dfs(n, sm):
    global ans

    # 가지치기 부분
    # 근데 테케가 적은 문제에선 가지치기가 오히려 시간복잡도를 높일 수 있음
    if ans <= sm-B:
        return

    if n == N:
        if sm >= B:
            ans = min(ans, sm-B)
        return

    dfs(n+1, sm+lst[n])  # 포함
    dfs(n+1, sm)        # 불포함


T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = N*10000
    dfs(0, 0)
    print(f"#{t} {ans}")
